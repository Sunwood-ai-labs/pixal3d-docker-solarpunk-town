---
name: pixal3d-image-to-3d
description: Generate 3D GLB models from input images with the Pixal3D Docker workflow in this repository. Use when Codex needs to convert PNG/JPG/WebP images into Pixal3D 3D assets, run the Gradio Pixal3D app, inspect or serve generated GLB outputs, batch-convert solarpunk town assets, tune FOV/background-removal settings, or troubleshoot Docker/NVIDIA/Hugging Face cache issues for Pixal3D image-to-3D generation.
---

# Pixal3D Image-to-3D

Use this skill to turn an image into a GLB model with the local Pixal3D Docker setup in this repository.

## Repository Assumptions

- Work from the repository root: `D:\Prj\pixal3d-docker-solarpunk-town`.
- Use Docker Compose as the primary runtime. The `pixal3d` service runs `inference.py`.
- Expect NVIDIA GPU support through Docker. If GPU access is unavailable, stop and report that Pixal3D generation cannot run in this setup.
- Keep generated assets under `outputs/generated_game_assets/` unless the user requests another location.
- Keep source images under `assets/generated_game_assets/` or `outputs/generated_game_assets/` when they are project assets.
- Do not commit `.cache/`; it contains model downloads and may contain local Hugging Face authentication material.

## Core Workflow

1. Confirm the input image path and desired output path.
2. Prefer isolated subject images with clean alpha. If the input already has a good transparent background, set `PIXAL3D_SKIP_REMBG=1`.
3. Build the Docker image if needed:

```powershell
docker compose build pixal3d
```

4. Run inference:

```powershell
$env:PIXAL3D_INPUT='outputs/generated_game_assets/solar_tree.png'
$env:PIXAL3D_OUTPUT='outputs/generated_game_assets/solar_tree.glb'
$env:PIXAL3D_FOV='0.2'
$env:PIXAL3D_SKIP_REMBG='1'
docker compose run --rm pixal3d
Remove-Item Env:PIXAL3D_INPUT,Env:PIXAL3D_OUTPUT,Env:PIXAL3D_FOV,Env:PIXAL3D_SKIP_REMBG -ErrorAction SilentlyContinue
```

5. Verify the GLB file exists and has a non-trivial file size:

```powershell
Get-Item outputs/generated_game_assets/solar_tree.glb | Select-Object FullName,Length,LastWriteTime
```

6. Serve the viewer when visual inspection is useful:

```powershell
docker compose up viewer
```

Open `http://127.0.0.1:8787/gallery.html` when inspecting the town gallery, or open a simple local viewer if the generated model is not wired into `gallery.html`.

## Input Image Guidance

- Use a centered, single-subject image with the object fully visible.
- Prefer square or near-square images.
- Prefer transparent PNG for game props and isolated objects.
- Avoid heavy shadows, cropped objects, multiple subjects, busy backgrounds, and text baked into the object.
- If background removal is needed, leave `PIXAL3D_SKIP_REMBG` unset or set it to `0`. This may require Hugging Face access for gated background-removal models.
- If background removal hurts an already-clean RGBA image, rerun with `PIXAL3D_SKIP_REMBG=1`.

## FOV Selection

- Start with `PIXAL3D_FOV=0.2` for the existing solarpunk asset style.
- If the model looks too flattened or distorted, try nearby values such as `0.15`, `0.25`, or `0.3`.
- Keep the original GLB when experimenting. Write variants with descriptive names such as `asset_fov025.glb`.

## Batch Conversion

For the existing solarpunk town batch, use:

```powershell
.\scripts\convert-solartown-assets.ps1 -Fov 0.2 -SkipRembg
```

Read the script before changing its asset list. Keep new batch entries explicit and avoid overwriting unrelated GLB files.

## Gradio App

When the user wants an interactive Pixal3D UI instead of CLI generation, run:

```powershell
docker compose --profile app up app
```

Open `http://127.0.0.1:7860`.

Use the app for manual previews, but prefer the CLI workflow for repeatable asset generation.

## Output Handling

- Pixal3D exports GLB with WebP texture extension enabled.
- Preserve the original output GLB. If applying post-processing such as tilt correction, create a new file such as `*_tilt_corrected.glb`.
- If using the existing town viewer, update `outputs/generated_game_assets/gallery.html` only when adding the model to the scene is part of the user request.
- For tilt-correction of the existing asset set, inspect and use `scripts/apply_tilt_correction.py`; it depends on an external `auto_tilt_correct_glb.py` tool in the user's Downloads folder by default.

## Troubleshooting

- Docker image missing: run `docker compose build pixal3d`.
- CUDA/GPU unavailable: check Docker Desktop/WSL2 NVIDIA support and `docker compose` GPU access before retrying.
- Model download or authentication failure: inspect `.cache/huggingface`, Hugging Face login state, and whether background removal is enabled.
- Out-of-memory errors: close other GPU workloads, retry, or reduce concurrent runs. Do not start multiple Pixal3D generations in parallel.
- Bad subject extraction: rerun with `PIXAL3D_SKIP_REMBG=1` for alpha PNGs, or prepare a cleaner isolated image.
- Poor model orientation: keep the raw GLB, create a corrected variant, and document the transform if applying deterministic post-processing.

## Reporting Back

When finished, report:

- Input image path.
- Output GLB path.
- Key settings used: FOV and background-removal mode.
- Whether Docker build/inference/viewer succeeded.
- Any residual quality issues that need visual review or reruns.
