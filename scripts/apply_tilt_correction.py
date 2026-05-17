from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


BASE = Path("outputs/generated_game_assets")
ORIGINAL_DIR = BASE / "models" / "original"
CORRECTED_DIR = BASE / "models" / "tilt_corrected"
REPORT_DIR = BASE / "reports"
INPUTS = [
    "mana_crystal.glb",
    "treasure_chest.glb",
    "energy_turret.glb",
    "mushroom_house.glb",
    "solar_tree.glb",
    "greenhouse_dome.glb",
    "wind_pod.glb",
    "market_stall.glb",
]


def default_tool_path() -> Path:
    return Path.home() / "Downloads" / "auto_tilt_correct_glb.py"


def load_tool(path: Path):
    spec = importlib.util.spec_from_file_location("auto_tilt_correct_glb", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser(description="Create non-destructive *_tilt_corrected.glb variants.")
    parser.add_argument("--tool", type=Path, default=default_tool_path(), help="Path to auto_tilt_correct_glb.py")
    parser.add_argument("--base", type=Path, default=BASE, help="Generated asset root directory")
    args = parser.parse_args()

    tool = load_tool(args.tool)
    results = []
    original_dir = args.base / "models" / "original"
    corrected_dir = args.base / "models" / "tilt_corrected"
    report_dir = args.base / "reports"
    corrected_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    for name in INPUTS:
        src = original_dir / name
        dst = corrected_dir / f"{src.stem}_tilt_corrected.glb"
        print(f"correcting {src} -> {dst}", flush=True)
        results.append(tool.correct_file(src, dst))

    report = report_dir / "tilt_correction_report.json"
    report.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
