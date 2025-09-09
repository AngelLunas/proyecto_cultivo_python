from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]

def get_excel_file_path() -> Path:
    return get_project_root() / "api" / "data" / "datos.xlsx"

def ensure_excel_exists() -> Path:
    path = get_excel_file_path()
    if not path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo Excel en: {path}\n"
            f"Edita api/config/paths.py si tu archivo está en otra ruta."
        )
    return path
