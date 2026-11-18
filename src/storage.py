import json
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_FILE = DATA_DIR / "rides.json"


def save_ride(ride_data, file_path=None):
    if file_path is None:
        file_path = DATA_FILE

    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    rides = load_rides(file_path)
    rides.append(ride_data)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(rides, file, indent=2, ensure_ascii=False)


def load_rides(file_path=None):
    if file_path is None:
        file_path = DATA_FILE

    file_path = Path(file_path)

    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)