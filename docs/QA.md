# QA Notes

## Requested Deliverables

- Publish-ready repository structure.
- Docker Compose setup for Pixal3D inference and viewer serving.
- Shared model/cache directories that are reusable across container rebuilds.
- Solarpunk town viewer and generated assets preserved as project artifacts.
- Public documentation in Japanese and English.

## Local Checks

- Static viewer URL: `http://127.0.0.1:8787/gallery.html`
- Last browser verification: 8 assets loaded, no console errors.
- Grounding check after facility scaling: house, market, solar tree, wind pod, and greenhouse report `groundClearance: 0`.
- Tilt-corrected viewer check: all 8 `*_tilt_corrected.glb` files loaded with HTTP 200 and no console errors.

## Publishing Guardrails

- `.cache/` is ignored and must not be committed.
- Verification screenshots named `*verified*.png` are ignored.
- Local scratch files under `outputs/generated_game_assets/workfiles/` are ignored.
- The current upstream Pixal3D remote should be replaced with a new project remote before pushing.
