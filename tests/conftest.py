# tests/conftest.py — añade la carpeta raíz del proyecto al inicio de sys.path
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]  # /ruta/a/kit_utiles
sys.path.insert(0, str(ROOT))               # ahora "import src.x" encontrará src/
