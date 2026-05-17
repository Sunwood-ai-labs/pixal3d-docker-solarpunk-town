# Docker Setup

This Docker setup is designed for repeatable Pixal3D inference with shared host caches.

## Requirements

- Docker Desktop with WSL2 backend on Windows, or Docker Engine on Linux.
- NVIDIA GPU support in Docker.
- Disk space for CUDA dependencies and model caches.
- Hugging Face access for gated background-removal models if `PIXAL3D_SKIP_REMBG=0`.

On Windows, initialize WSL2 first:

```powershell
wsl --install --no-distribution
wsl --set-default-version 2
```

## Build

From the repository root:

```powershell
docker compose build pixal3d
```

The image builds from `nvidia/cuda:12.4.1-devel-ubuntu22.04`, clones `microsoft/TRELLIS.2`, installs CUDA extensions, installs Pixal3D requirements, and adds the NATTEN wheel used by the demo.

## Run Inference

```powershell
$env:PIXAL3D_INPUT='outputs/generated_game_assets/images/sources/solar_tree.png'
$env:PIXAL3D_OUTPUT='outputs/generated_game_assets/models/original/solar_tree.glb'
$env:PIXAL3D_FOV='0.2'
docker compose run --rm pixal3d
```

For images that already have a good alpha channel:

```powershell
$env:PIXAL3D_SKIP_REMBG='1'
docker compose run --rm pixal3d
Remove-Item Env:PIXAL3D_SKIP_REMBG
```

## Run the Static Viewer

```powershell
docker compose up viewer
```

Open `http://127.0.0.1:8787/gallery.html`.

## Run the Gradio App

```powershell
docker compose --profile app up app
```

Open `http://127.0.0.1:7860`.

## Shared Cache Mounts

The Compose file keeps these directories outside the container:

```text
.cache/huggingface
.cache/torch
.cache/xdg
```

They are ignored by Git and should not be published. They can contain large model files and local authentication material.
