Param(
  [int]$Port = 3005
)
$ErrorActionPreference = "Stop"

# Resolve root to this script's folder
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

# Start simple HTTP server (Python) in a new window
$serverCmd = "python -m http.server $Port"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd `"$Root`"; $serverCmd" | Out-Null

Start-Sleep -Seconds 2
$Url = "http://localhost:$Port"
Write-Host "Server running at $Url"
Start-Process $Url
