# Asset Inventory

This demo keeps the finished scene under `outputs/generated_game_assets/`.

## Viewer

- `gallery.html` - main Three.js viewer
- `field.html` - synchronized copy of the main viewer
- `field_panorama.png` - solarpunk panorama background
- `preview.png` - README preview image
- `preview_tilt_corrected.png` - README preview after non-destructive pose correction

## GLB Assets

| File | Role |
|---|---|
| `mana_crystal.glb` | Central energy core |
| `treasure_chest.glb` | Storage chest |
| `energy_turret.glb` | Utility turret |
| `mushroom_house.glb` | Main house |
| `solar_tree.glb` | Solar charging tree |
| `greenhouse_dome.glb` | Garden greenhouse |
| `wind_pod.glb` | Wind power pod |
| `market_stall.glb` | Community market |

## Tilt-Corrected GLB Assets

The viewer references these non-destructive corrected variants:

| File | Source |
|---|---|
| `mana_crystal_tilt_corrected.glb` | `mana_crystal.glb` |
| `treasure_chest_tilt_corrected.glb` | `treasure_chest.glb` |
| `energy_turret_tilt_corrected.glb` | `energy_turret.glb` |
| `mushroom_house_tilt_corrected.glb` | `mushroom_house.glb` |
| `solar_tree_tilt_corrected.glb` | `solar_tree.glb` |
| `greenhouse_dome_tilt_corrected.glb` | `greenhouse_dome.glb` |
| `wind_pod_tilt_corrected.glb` | `wind_pod.glb` |
| `market_stall_tilt_corrected.glb` | `market_stall.glb` |

`tilt_correction_report.json` records the correction angle, bounds, and support-plane diagnostics for each model.

## Source Images

The first four source images are in `assets/generated_game_assets/`.
The later solarpunk source PNGs are in `outputs/generated_game_assets/`.

Verification screenshots named `*verified*.png` are local QA artifacts and are ignored by Git.
