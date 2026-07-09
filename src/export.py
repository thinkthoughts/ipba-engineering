from pathlib import Path
from zipfile import ZipFile

def find_repo_root() -> Path:
    cwd = Path.cwd()
    if cwd.name == "notebooks":
        return cwd.parent
    return cwd

def finalize_notebook(
    notebook: str = "00_context.ipynb",
    zip_name: str = "benefits-distribution-00-context-outputs.zip",
    folders=("figures", "results", "data"),
):
    root = find_repo_root()
    zip_path = root / zip_name
    notebook_path = root / "notebooks" / notebook

    with ZipFile(zip_path, "w") as z:
        for folder_name in folders:
            folder = root / folder_name
            if folder.exists():
                for file in folder.rglob("*"):
                    if file.is_file():
                        z.write(file, file.relative_to(root))

    print(f"Created outputs archive: {zip_path}")

    try:
        from IPython.display import FileLink, display
        if notebook_path.exists():
            print("Notebook:")
            display(FileLink(str(notebook_path)))
        print("Generated outputs:")
        display(FileLink(str(zip_path)))
    except Exception:
        print("Notebook:", notebook_path)
        print("Generated outputs:", zip_path)

    return zip_path
