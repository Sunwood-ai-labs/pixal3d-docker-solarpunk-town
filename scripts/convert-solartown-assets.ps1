param(
  [string]$Fov = "0.2",
  [switch]$SkipRembg
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$assets = @(
  @{ Input = "outputs/generated_game_assets/solar_tree.png"; Output = "outputs/generated_game_assets/solar_tree.glb" },
  @{ Input = "outputs/generated_game_assets/greenhouse_dome.png"; Output = "outputs/generated_game_assets/greenhouse_dome.glb" },
  @{ Input = "outputs/generated_game_assets/wind_pod.png"; Output = "outputs/generated_game_assets/wind_pod.glb" },
  @{ Input = "outputs/generated_game_assets/market_stall.png"; Output = "outputs/generated_game_assets/market_stall.glb" }
)

foreach ($asset in $assets) {
  Write-Host "Converting $($asset.Input) -> $($asset.Output)"
  $env:PIXAL3D_INPUT = $asset.Input
  $env:PIXAL3D_OUTPUT = $asset.Output
  $env:PIXAL3D_FOV = $Fov
  if ($SkipRembg) {
    $env:PIXAL3D_SKIP_REMBG = "1"
  }
  docker compose run --rm pixal3d
}

Remove-Item Env:PIXAL3D_INPUT -ErrorAction SilentlyContinue
Remove-Item Env:PIXAL3D_OUTPUT -ErrorAction SilentlyContinue
Remove-Item Env:PIXAL3D_FOV -ErrorAction SilentlyContinue
if ($SkipRembg) {
  Remove-Item Env:PIXAL3D_SKIP_REMBG -ErrorAction SilentlyContinue
}
