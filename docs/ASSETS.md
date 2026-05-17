# Asset Inventory

This demo keeps the finished scene under `outputs/generated_game_assets/`.

## Directory Layout

```text
outputs/generated_game_assets/
  gallery.html
  field.html
  models/
    original/
    tilt_corrected/
  images/
    panorama/
    previews/
    sources/
  reports/
  workfiles/        local-only scratch files, ignored by Git
```

## Viewer

- `gallery.html` - main Three.js viewer
- `field.html` - synchronized copy of the main viewer
- `images/panorama/field_panorama.png` - solarpunk panorama background
- `images/panorama/solarpunk_panorama_source.png` - generated panorama source
- `images/previews/preview.png` - early README preview image
- `images/previews/preview_tilt_corrected.png` - README preview after non-destructive pose correction

## Original GLB Assets

| File | Role |
|---|---|
| `models/original/mana_crystal.glb` | Central energy core |
| `models/original/treasure_chest.glb` | Storage chest |
| `models/original/energy_turret.glb` | Utility turret |
| `models/original/mushroom_house.glb` | Main house |
| `models/original/solar_tree.glb` | Solar charging tree |
| `models/original/greenhouse_dome.glb` | Garden greenhouse |
| `models/original/wind_pod.glb` | Wind power pod |
| `models/original/market_stall.glb` | Community market |

## Tilt-Corrected GLB Assets

The viewer references these non-destructive corrected variants:

| File | Source |
|---|---|
| `models/tilt_corrected/mana_crystal_tilt_corrected.glb` | `models/original/mana_crystal.glb` |
| `models/tilt_corrected/treasure_chest_tilt_corrected.glb` | `models/original/treasure_chest.glb` |
| `models/tilt_corrected/energy_turret_tilt_corrected.glb` | `models/original/energy_turret.glb` |
| `models/tilt_corrected/mushroom_house_tilt_corrected.glb` | `models/original/mushroom_house.glb` |
| `models/tilt_corrected/solar_tree_tilt_corrected.glb` | `models/original/solar_tree.glb` |
| `models/tilt_corrected/greenhouse_dome_tilt_corrected.glb` | `models/original/greenhouse_dome.glb` |
| `models/tilt_corrected/wind_pod_tilt_corrected.glb` | `models/original/wind_pod.glb` |
| `models/tilt_corrected/market_stall_tilt_corrected.glb` | `models/original/market_stall.glb` |

`reports/tilt_correction_report.json` records the correction angle, bounds, and support-plane diagnostics for each model.

## Source Images

- The first four source images are in `assets/generated_game_assets/`.
- Later solarpunk source PNGs are in `outputs/generated_game_assets/images/sources/`.
- Verification screenshots named `*verified*.png` are local QA artifacts and are ignored by Git.
