from src.storage import load_rides, save_ride


def test_save_and_load_ride(tmp_path):
    test_file = tmp_path / "rides.json"

    ride_data = {
        "started_at": "2026-11-17T12:00:00",
        "finished_at": "2026-11-17T12:00:10",
        "segments": [
            {
                "status": "stopped",
                "seconds": 10.0,
            }
        ],
        "total": 0.20,
    }

    save_ride(ride_data, test_file)

    rides = load_rides(test_file)

    assert ride_data in rides

def test_load_rides_returns_empty_list_when_file_does_not_exist(tmp_path):
    test_file = tmp_path / "missing.json"

    rides = load_rides(test_file)

    assert rides == []