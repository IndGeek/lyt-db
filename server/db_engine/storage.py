import json
from pathlib import Path

class StorageEngine:
    def __init__(self, db_path="data"):
        self.db_path = Path(db_path)
        self.db_path.mkdir(parents=True, exist_ok=True)

    def save(self, db_name, data):
        db_file = self.db_path / f"{db_name}.lyt"
        with open(db_file, "w") as f:
            json.dump(data, f)

    def load(self, db_name):
        db_file = self.db_path / f"{db_name}.lyt"
        if not db_file.exists():
            raise FileNotFoundError(f"Database '{db_name}' does not exist.")
        with open(db_file, "r") as f:
            return json.load(f)
