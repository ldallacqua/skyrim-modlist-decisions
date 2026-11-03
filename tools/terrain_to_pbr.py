#!/usr/bin/env python3
"""Turns an ENB complex parallax landscape texture into a Community Shaders PBR landscape set.

  python -I tools/terrain_to_pbr.py <colour.dds> <normal.dds> <output folder> <name> --match <PBR albedo.dds>
         [--height alpha|<height.dds>] [--brightness 1.0] [--height-size 2048] [--copies <name> ...]

It writes four maps into the output folder, in the formats TomatoRim's PBR landscapes use:
- <name>.dds, the albedo, BC7 sRGB. Community Shaders reads full PBR terrain colour as linear, so the
  colour map is scaled in linear light until its mean brightness matches --match, the PBR texture it
  replaces. Highlights roll off instead of clipping. --brightness scales the target.
- <name>_n.dds, the normal map's RGB, BC7.
- <name>_p.dds, the height, BC4. ENB terrain parallax keeps it in the colour map's alpha, the default here.
- <name>_rmaos.dds, BC1: roughness from 0.96 on dark dirt to 0.86 on the brightest stones, metal 0,
  AO 1 because the colour map already carries its shading, and specular 1, which the texture set's
  specularLevel scales.
--copies writes the albedo again under other names, for texture sets that each point at their own
colour map. Every mip of every map is checked against the full-size level after compression.
Needs numpy, and Texconv from SSEEdit's scripts folder (TEXCONV overrides the path).
"""
import argparse
import os
import shutil
import struct
import subprocess
import tempfile

import numpy as np

TEXCONV = os.environ.get("TEXCONV", r"C:\Modding\TOOLS\SSEEdit\Edit Scripts\Texconvx64.exe")
SRGB_FORMATS = {29, 72, 75, 78, 91, 93, 99}
FORMAT_NAMES = {71: "BC1", 80: "BC4", 98: "BC7", 99: "BC7 sRGB"}


def header(path):
    data = open(path, "rb").read(148)
    height, width = struct.unpack_from("<II", data, 12)
    fourcc = data[84:88]
    dxgi = struct.unpack_from("<I", data, 128)[0] if fourcc == b"DX10" else {b"BC4U": 80, b"ATI1": 80, b"DXT1": 71}.get(fourcc)
    return width, height, dxgi


def texconv(args):
    result = subprocess.run([TEXCONV, "-nologo", "-y"] + args, capture_output=True, text=True)
    if result.returncode != 0 or "FAILED" in result.stdout:
        raise SystemExit(f"Texconv failed: {result.stdout[-1500:]}{result.stderr[-1500:]}")


def decode(path):
    """The top mip as an (h, w, 4) uint8 array, with no colour-space change."""
    srgb = header(path)[2] in SRGB_FORMATS
    with tempfile.TemporaryDirectory() as folder:
        texconv(["-f", "R8G8B8A8_UNORM_SRGB" if srgb else "R8G8B8A8_UNORM", "-m", "1", "-o", folder, path]
                + (["-srgbi", "-srgbo"] if srgb else []))
        data = open(os.path.join(folder, os.path.basename(path)), "rb").read()
    height, width = struct.unpack_from("<II", data, 12)
    offset = 128 + (20 if data[84:88] == b"DX10" else 0)
    return np.frombuffer(data, np.uint8, width * height * 4, offset).reshape(height, width, 4).copy()


def encode(rgba, target, dxgi_format, srgb=False):
    """Writes an (h, w, 4) uint8 array to target, compressed with a full mip chain."""
    height, width = rgba.shape[:2]
    with tempfile.TemporaryDirectory() as folder:
        raw = os.path.join(folder, os.path.basename(target))
        pixel_format = struct.pack("<II4sIIIII", 32, 0x41, b"\0\0\0\0", 32, 0xFF, 0xFF00, 0xFF0000, 0xFF000000)
        head = struct.pack("<4sIIIIIII44s", b"DDS ", 124, 0x100F, height, width, width * 4, 0, 1, b"\0" * 44)
        with open(raw, "wb") as file:
            file.write(head + pixel_format + struct.pack("<IIIII", 0x1000, 0, 0, 0, 0) + np.ascontiguousarray(rgba).tobytes())
        texconv(["-f", dxgi_format, "-m", "0", "-o", os.path.dirname(target), raw] + (["-srgbi", "-srgbo"] if srgb else []))
    # Texconv writes the extension as .DDS, and this build has no -l to stop it
    written = next(name for name in os.listdir(os.path.dirname(target)) if name.lower() == os.path.basename(target).lower())
    os.replace(os.path.join(os.path.dirname(target), written), target)
    check_mips(target)


def check_mips(path):
    """Stops if any mip's channel means stray from the top mip's. Texconv once wrote black mips under a full-size
    level that was fine, because it weights colour by alpha when it shrinks, and the alpha was 0."""
    srgb = header(path)[2] in SRGB_FORMATS
    with tempfile.TemporaryDirectory() as folder:
        texconv(["-f", "R8G8B8A8_UNORM_SRGB" if srgb else "R8G8B8A8_UNORM", "-o", folder, path] + (["-srgbi", "-srgbo"] if srgb else []))
        data = open(os.path.join(folder, os.listdir(folder)[0]), "rb").read()
    height, width = struct.unpack_from("<II", data, 12)
    mips = struct.unpack_from("<I", data, 28)[0]
    offset = 128 + (20 if data[84:88] == b"DX10" else 0)
    top = None
    for level in range(mips):
        size = width * height * 4
        means = np.frombuffer(data, np.uint8, size, offset).reshape(-1, 4)[:, :3].mean(0, dtype=np.float64) / 255
        offset += size
        top = means if top is None else top
        if np.abs(means - top).max() > 0.06:
            raise SystemExit(f"{os.path.basename(path)}: mip {level} ({width}x{height}) has RGB means {means.round(3)}, "
                             f"against {top.round(3)} at full size")
        width, height = max(1, width // 2), max(1, height // 2)


def to_linear(srgb):
    return np.where(srgb <= 0.04045, srgb / 12.92, ((srgb + 0.055) / 1.055) ** 2.4)


def to_srgb(linear):
    linear = np.clip(linear, 0, 1)
    return np.where(linear <= 0.0031308, linear * 12.92, 1.055 * linear ** (1 / 2.4) - 0.055)


def luminance(linear):
    return linear[..., 0] * 0.2126 + linear[..., 1] * 0.7152 + linear[..., 2] * 0.0722


def shrink(channel, size):
    factor = channel.shape[0] // size
    if factor <= 1:
        return channel
    return channel.reshape(size, factor, size, factor).mean(axis=(1, 3))


def as_bytes(values):
    return np.clip(np.round(values * 255), 0, 255).astype(np.uint8)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("colour")
    parser.add_argument("normal")
    parser.add_argument("output")
    parser.add_argument("name")
    parser.add_argument("--match", required=True, help="the PBR albedo whose mean brightness to match")
    parser.add_argument("--height", default="alpha", help="alpha (the colour map's alpha) or a height map")
    parser.add_argument("--brightness", type=float, default=1.0)
    parser.add_argument("--height-size", type=int, default=2048)
    parser.add_argument("--copies", nargs="*", default=[])
    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    out = lambda suffix: os.path.join(args.output, f"{args.name}{suffix}.dds")

    colour = decode(args.colour)
    linear = to_linear(colour[..., :3].astype(np.float32) / 255)
    reference = to_linear(decode(args.match)[..., :3].astype(np.float32) / 255)
    gain = luminance(reference).mean() / luminance(linear).mean() * args.brightness
    albedo = np.maximum(linear * gain, 0.005)
    knee = 0.8
    albedo = np.where(albedo > knee, knee + (1 - knee) * np.tanh((albedo - knee) / (1 - knee)), albedo)
    rgba = np.zeros(colour.shape, np.uint8)
    rgba[..., :3] = as_bytes(to_srgb(albedo))
    # Opaque: PBR terrain ignores this alpha, but Texconv weights colour by it when it builds the mips
    rgba[..., 3] = 255
    encode(rgba, out(""), "BC7_UNORM_SRGB", srgb=True)
    print(f"albedo: mean luminance {luminance(linear).mean():.4f} -> {luminance(albedo).mean():.4f} "
          f"(reference {luminance(reference).mean():.4f}), gain {gain:.2f}, {(linear * gain > knee).mean():.2%} of values rolled off")

    normal = decode(args.normal)
    normal[..., 3] = 255
    encode(normal, out("_n"), "BC7_UNORM")

    height = colour[..., 3] if args.height == "alpha" else decode(args.height)[..., 0]
    height = shrink(height.astype(np.float32) / 255, min(args.height_size, height.shape[0]))
    encode(np.repeat(as_bytes(height)[..., None], 4, axis=2), out("_p"), "BC4_UNORM")
    print(f"height: {height.shape[0]}px, mean {height.mean():.3f}, spread (std) {height.std():.3f}")

    size = height.shape[0]
    brightness = shrink(luminance(albedo), size)
    low, high = np.percentile(brightness, [5, 99.5])
    roughness = 0.96 - 0.10 * np.clip((brightness - low) / (high - low), 0, 1)
    rmaos = np.stack([as_bytes(roughness), np.zeros_like(roughness, np.uint8),
                      np.full(roughness.shape, 255, np.uint8), np.full(roughness.shape, 255, np.uint8)], axis=2)
    encode(rmaos, out("_rmaos"), "BC1_UNORM")
    print(f"roughness: mean {roughness.mean():.3f}, from {roughness.min():.2f} to {roughness.max():.2f}")

    for copy in args.copies:
        shutil.copyfile(out(""), os.path.join(args.output, f"{copy}.dds"))
    for suffix in ["", "_n", "_p", "_rmaos"]:
        width, height_px, dxgi = header(out(suffix))
        print(f"wrote {args.name}{suffix}.dds  {width}x{height_px} {FORMAT_NAMES.get(dxgi, dxgi)}  {os.path.getsize(out(suffix)) / 2**20:.1f} MB")
    if args.copies:
        print(f"copied the albedo to {len(args.copies)} names: {', '.join(args.copies)}")


if __name__ == "__main__":
    main()
