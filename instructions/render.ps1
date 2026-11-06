# Windows: rebuild HUSH_Quick_Start_Guide.pdf from guide.html with headless Edge or Chrome.
$d = $PSScriptRoot
$pdf = Join-Path $d "HUSH_Quick_Start_Guide.pdf"
$candidates = @(
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)
$browser = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $browser) { Write-Error "Edge or Chrome not found. Open guide.html in a browser and Print > Save as PDF instead."; exit 1 }
Start-Process -FilePath $browser -Wait -ArgumentList @("--headless=new","--disable-gpu","--no-pdf-header-footer","--user-data-dir=$env:TEMP\hush-pdf","--print-to-pdf=$pdf","file:///$($d -replace '\\','/')/guide.html")
Write-Output "Wrote $pdf"
