"""Copy Quarto output into GitHub Pages without changing the preview root."""

from pathlib import Path
import shutil


project = Path(__file__).resolve().parent.parent
shutil.copytree(project / "_site", project / "docs" / "site", dirs_exist_ok=True)
