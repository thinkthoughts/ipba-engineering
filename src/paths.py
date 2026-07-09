from pathlib import Path

def find_repo_root() -> Path:
    cwd = Path.cwd()
    if cwd.name == "notebooks":
        return cwd.parent
    return cwd

ROOT = find_repo_root()
FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"
DATA = ROOT / "data"
NOTEBOOKS = ROOT / "notebooks"

for path in [FIGURES, RESULTS, DATA, NOTEBOOKS]:
    path.mkdir(parents=True, exist_ok=True)
