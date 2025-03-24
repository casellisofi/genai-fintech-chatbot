# -----------------------------------------------------------------------------------
# JSON LOADER MODULE
# -----------------------------------------------------------------------------------
# Utilidad para cargar archivos JSON.
# -----------------------------------------------------------------------------------

from pathlib import Path
import json

def load_json(file_path: Path) -> dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
