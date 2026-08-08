import os
from pathlib import Path

from dotenv import load_dotenv


# Racine du backend
BASE_DIR = Path(__file__).resolve().parent


# Charger le fichier .env situé à la racine du projet
ENV_PATH = BASE_DIR.parent / ".env"

load_dotenv(ENV_PATH)


# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY n'est pas définie dans le fichier .env"
    )


GEMINI_MODEL = "gemini-3.6-flash"


# Dossiers
UPLOADS_DIR = BASE_DIR / "uploads"
OUTPUTS_DIR = BASE_DIR / "outputs"


UPLOADS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)