# Windows: rebuild HUSH_A4_Submission_DRAFT.pdf.
# Needs Edge or Chrome, and Python 3 with pypdf (pip install pypdf).
$d = $PSScriptRoot
$repo = Split-Path $d -Parent
# Pick the first Python that can actually import pypdf (skips the Windows Store "python" stub).
$py = @("python", "py", "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe") |
  Where-Object { (Get-Command $_ -ErrorAction SilentlyContinue) -and ((& $_ -c "import pypdf; print('ok')" 2>$null) -eq "ok") } |
  Select-Object -First 1
if (-not $py) { Write-Error "Python not found."; exit 1 }
$browser = @(
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $browser) { Write-Error "Edge or Chrome not found."; exit 1 }

& $py -X utf8 (Join-Path $d "make_part3.py") $repo
New-Item -ItemType Directory -Force (Join-Path $d "out") | Out-Null
foreach ($p in "part1", "part2", "part3") {
  Start-Process -FilePath $browser -Wait -ArgumentList @("--headless=new", "--disable-gpu", "--no-pdf-header-footer",
    "--user-data-dir=$env:TEMP\hush-submission-pdf", "--print-to-pdf=$d\out\$p.pdf", "file:///$($d -replace '\\','/')/$p.html")
}
& $py -X utf8 (Join-Path $d "merge.py") $d (Join-Path $repo "instructions\HUSH_Quick_Start_Guide.pdf") (Join-Path $d "slides\W11-presentation.pdf")
