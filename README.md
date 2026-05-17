<div align="center">

# Solarpunk Pocket Town with Pixal3D

Image-generated game props converted into GLB assets and arranged in a small interactive Three.js town.

[日本語](README.ja.md) · [Original Pixal3D project](https://ldyang694.github.io/projects/pixal3d/) · [Pixal3D models](https://huggingface.co/TencentARC/Pixal3D)

</div>

![Solarpunk town preview](outputs/generated_game_assets/images/previews/preview_tilt_corrected.png)

## ✨ What This Repo Contains

This repository is a public-ready demo project built on top of Tencent ARC's Pixal3D codebase.

- A Docker Compose setup for Windows/WSL2/Linux hosts with NVIDIA GPUs.
- Shared host caches for Hugging Face, Torch, and XDG data so large model files survive container rebuilds.
- Eight generated GLB game assets arranged in `outputs/generated_game_assets/gallery.html`.
- Non-destructive tilt-corrected GLB variants used by the viewer.
- A static Three.js viewer served locally on port `8787`.
- Local compatibility patches used to run Pixal3D in this environment.

The upstream Pixal3D research code, citation, and license are preserved. This repo adds a solarpunk town demo and operational Docker packaging around it.

## 🏙️ Demo Assets

The town currently includes:

| Asset | Source | 3D output |
|---|---|---|
| Mana crystal / energy core | `assets/generated_game_assets/mana_crystal_alpha.png` | `outputs/generated_game_assets/models/original/mana_crystal.glb` |
| Treasure chest / storage | `assets/generated_game_assets/treasure_chest_alpha.png` | `outputs/generated_game_assets/models/original/treasure_chest.glb` |
| Energy turret / utility node | `assets/generated_game_assets/energy_turret_alpha.png` | `outputs/generated_game_assets/models/original/energy_turret.glb` |
| Mushroom home | `assets/generated_game_assets/mushroom_house_alpha.png` | `outputs/generated_game_assets/models/original/mushroom_house.glb` |
| Solar tree | `outputs/generated_game_assets/images/sources/solar_tree.png` | `outputs/generated_game_assets/models/original/solar_tree.glb` |
| Greenhouse dome | `outputs/generated_game_assets/images/sources/greenhouse_dome.png` | `outputs/generated_game_assets/models/original/greenhouse_dome.glb` |
| Wind pod | `outputs/generated_game_assets/images/sources/wind_pod.png` | `outputs/generated_game_assets/models/original/wind_pod.glb` |
| Market stall | `outputs/generated_game_assets/images/sources/market_stall.png` | `outputs/generated_game_assets/models/original/market_stall.glb` |

The viewer uses `*_tilt_corrected.glb` variants. The original GLB files are kept next to them for comparison and rollback.

Open `outputs/generated_game_assets/gallery.html` through the viewer service to orbit the scene, switch focus targets, and inspect the final layout.

## 🚀 Quick Start

### 1. Prerequisites

- Windows + WSL2 + Docker Desktop, or Linux with Docker Engine.
- NVIDIA GPU with the NVIDIA Container Toolkit available to Docker.
- Enough disk space for CUDA/PyTorch/Pixal3D/TRELLIS model caches.
- Hugging Face access for gated background-removal models when `PIXAL3D_SKIP_REMBG=0`.

### 2. Build the Pixal3D image

```powershell
docker compose build pixal3d
```

The image is large. It installs CUDA-enabled PyTorch, TRELLIS.2, Pixal3D dependencies, CUDA extensions, `utils3d`, and the NATTEN wheel used by this setup.

### 3. Serve the finished town viewer

```powershell
docker compose up viewer
```

Then open:

```text
http://127.0.0.1:8787/gallery.html
```

### 4. Convert an image into GLB

```powershell
$env:PIXAL3D_INPUT='outputs/generated_game_assets/images/sources/solar_tree.png'
$env:PIXAL3D_OUTPUT='outputs/generated_game_assets/models/original/solar_tree.glb'
$env:PIXAL3D_FOV='0.2'
docker compose run --rm pixal3d
```

For already-isolated RGBA images, you can skip background removal:

```powershell
$env:PIXAL3D_SKIP_REMBG='1'
docker compose run --rm pixal3d
Remove-Item Env:PIXAL3D_SKIP_REMBG
```

### 5. Run the Gradio app

```powershell
docker compose --profile app up app
```

Then open:

```text
http://127.0.0.1:7860
```

## 🧠 Shared Model Cache

The Compose file mounts these host directories into the container:

```text
.cache/huggingface -> /workspace/.cache/huggingface
.cache/torch       -> /workspace/.cache/torch
.cache/xdg         -> /workspace/.cache/xdg
```

These directories are intentionally ignored by Git. They let you rebuild containers or run sibling containers without downloading large models again.

## 📁 Repository Layout

```text
assets/generated_game_assets/     Source images for the first generated props
outputs/generated_game_assets/    Organized viewer, model, image, and report assets
docker/Dockerfile                 CUDA/PyTorch/Pixal3D build image
docker-compose.yml                Inference, Gradio app, and static viewer services
docker/README.md                  Docker-specific notes
pixal3d/                          Pixal3D library code
inference.py                      CLI image-to-GLB entrypoint
app.py                            Gradio app entrypoint
```

## ⚠️ Publishing Notes

The current Git remote may still point at the upstream Pixal3D repository. Before pushing publicly, create a new repository and set it as `origin`:

```powershell
git remote remove origin
git remote add origin https://github.com/<your-user>/<your-repo>.git
git push -u origin master
```

Do not commit `.cache/`; it may contain large model files and local Hugging Face credentials.

## 📄 Attribution

This project is based on:

- [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D)
- [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)

If you use the Pixal3D research code, cite the original paper:

```bibtex
@article{li2026pixal3d,
    title={Pixal3D: Pixel-Aligned 3D Generation from Images},
    author={Li, Dong-Yang and Zhao, Wang and Chen, Yuxin and Hu, Wenbo and Guo, Meng-Hao and Zhang, Fang-Lue and Shan, Ying and Hu, Shi-Min},
    journal={arXiv preprint arXiv:2605.10922},
    year={2026}
}
```
