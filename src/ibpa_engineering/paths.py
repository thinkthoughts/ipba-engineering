from __future__ import annotations

from pathlib import Path


def find_repo_root(start: str | Path | None = None) -> Path:
    current = Path(start or Path.cwd()).resolve()

    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").exists() and (candidate / "src").exists():
            return candidate

    if current.name == "notebooks":
        return current.parent

    return current


ROOT = find_repo_root()
FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"
DATA = ROOT / "data"
NOTEBOOKS = ROOT / "notebooks"


def initialize_directories() -> None:
    for directory in (FIGURES, RESULTS, DATA, NOTEBOOKS):
        directory.mkdir(parents=True, exist_ok=True)
