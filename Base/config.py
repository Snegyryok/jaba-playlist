from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "track-base.db"

DATABASE_URL = f"sqlite:///{DB_PATH}"

print (BASE_DIR)