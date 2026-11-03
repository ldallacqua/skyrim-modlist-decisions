# Runs an MO2 executable through MO2's virtual file system without anyone at the keyboard.
#
#   tools\mo2-run.ps1 -Title PGPatcher -Arguments '--autostart'
#   tools\mo2-run.ps1 -Sort                      LOOT auto-sort, with its masterlist update off for the run
#   tools\mo2-run.ps1 -RegeneratePGPatcher       disable the output, run PGPatcher, re-enable it, then sort
#
# Arguments are set only for this run and restored afterwards. Windows the tool leaves open, such as
# PGPatcher's "Generation Complete" or LOOT's "Sorting made no changes", are read aloud and closed with
# their OK button. MO2 must be closed, and it asks no Steam question for tools listed under [DialogChoices].
param(
    [string] $Title,
    [string] $Arguments = '',
    [switch] $Sort,
    [switch] $RegeneratePGPatcher,
    [int] $TimeoutSeconds = 600
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes
$tools = $PSScriptRoot
$mo2 = if ($env:MO2_DIR) { $env:MO2_DIR } else { 'C:\Modding\MO2' }

function Invoke-Mo2Py([string[]] $arguments) {
    python -X utf8 (Join-Path $tools 'mo2.py') @arguments
    if ($LASTEXITCODE -ne 0) { throw "mo2.py $($arguments -join ' ') failed" }
}

function Close-OkWindows([string] $process) {
    $automation = [System.Windows.Automation.AutomationElement]
    foreach ($p in Get-Process $process -ErrorAction SilentlyContinue) {
        $byProcess = New-Object System.Windows.Automation.PropertyCondition($automation::ProcessIdProperty, $p.Id)
        foreach ($window in $automation::RootElement.FindAll([System.Windows.Automation.TreeScope]::Children, $byProcess)) {
            $byName = New-Object System.Windows.Automation.PropertyCondition($automation::NameProperty, 'OK')
            $ok = $window.FindAll([System.Windows.Automation.TreeScope]::Descendants, $byName)
            if ($ok.Count -gt 0) {
                $text = $window.FindAll([System.Windows.Automation.TreeScope]::Descendants, [System.Windows.Automation.Condition]::TrueCondition) |
                    Where-Object { $_.Current.ControlType.ProgrammaticName -eq 'ControlType.Text' } | ForEach-Object { $_.Current.Name }
                Write-Output "$process says: $(($text -join ' ') -replace '\s+', ' ')"
                $ok[0].GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern).Invoke()
            }
        }
    }
}

function Invoke-Executable([string] $title, [string] $arguments) {
    if (Get-Process ModOrganizer -ErrorAction SilentlyContinue) { throw 'Close MO2 first: it rewrites its settings on exit.' }
    $previous = ((Invoke-Mo2Py @('exe-args', $title)) -split '=', 2)[1]
    $process = [IO.Path]::GetFileNameWithoutExtension((Select-String -LiteralPath "$mo2\ModOrganizer.ini" -Pattern '^(\d+)\\binary=(.*)$' |
        Where-Object { (Select-String -LiteralPath "$mo2\ModOrganizer.ini" -Pattern "^$($_.Matches[0].Groups[1].Value)\\title=$([regex]::Escape($title))$") } |
        Select-Object -First 1).Matches[0].Groups[2].Value)
    Invoke-Mo2Py @('exe-args', $title, "--set=$arguments") | Out-Null
    try {
        Start-Process -FilePath "$mo2\ModOrganizer.exe" -ArgumentList "`"moshortcut://:$title`""
        $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
        Start-Sleep -Seconds 8
        while (Get-Process ModOrganizer, $process -ErrorAction SilentlyContinue) {
            if ((Get-Date) -gt $deadline) { throw "$title still running after $TimeoutSeconds s" }
            Close-OkWindows $process
            Start-Sleep -Seconds 3
        }
    } finally {
        # MO2 saves its settings when it exits, so the restore waits until it has
        Invoke-Mo2Py @('exe-args', $title, "--set=$previous") | Out-Null
    }
}

function Invoke-Sort {
    $masterlist = Join-Path $env:LOCALAPPDATA 'LOOT\games\Skyrim Special Edition\masterlist.yaml'
    Invoke-Mo2Py @('loot-update', 'off') | Out-Null
    try { Invoke-Executable 'LOOT' '--game=\"Skyrim Special Edition\" --auto-sort' }
    finally { Invoke-Mo2Py @('loot-update', 'on') | Out-Null }
    Get-Content -LiteralPath (Join-Path $env:LOCALAPPDATA 'LOOT\LOOTDebugLog.txt') -Tail 1
    if ((Get-Item -LiteralPath $masterlist).Length -eq 0) { throw 'LOOT left an empty masterlist; see AGENTS.md' }
}

if ($RegeneratePGPatcher) {
    Invoke-Mo2Py @('disable', 'PGPatcher - Outputs')
    Invoke-Executable 'PGPatcher' '--autostart'
    Select-String -LiteralPath "$mo2\mods\PGPatcher\PGPatcher\log\PGPatcher.log" -Pattern '\[error\]|TruePBR entries|took' | ForEach-Object Line
    Invoke-Mo2Py @('enable', 'PGPatcher - Outputs')
    Invoke-Mo2Py @('enable-plugins', 'PGPatcher - Outputs')
    Invoke-Sort
    Invoke-Mo2Py @('pgpatcher-check')
} elseif ($Sort) {
    Invoke-Sort
} elseif ($Title) {
    Invoke-Executable $Title $Arguments
} else {
    Get-Content -LiteralPath $PSCommandPath -TotalCount 9
}
