from pathlib import Path


def find_repo_root() -> Path:
    root = Path.cwd()

    if root.name == "notebooks":
        root = root.parent

    return root


ROOT = find_repo_root()

FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"
DATA = ROOT / "data"
NOTEBOOKS = ROOT / "notebooks"


def initialize_directories() -> None:
    for directory in (
        FIGURES,
        RESULTS,
        DATA,
        NOTEBOOKS,
    ):
        directory.mkdir(
            parents=True,
            exist_ok=True,
        )
