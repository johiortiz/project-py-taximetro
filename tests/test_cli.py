from src.cli import (
    format_duration,
    get_history_summary,
    get_total_duration,
)


def test_format_duration():
    assert format_duration(10) == "0h 0m 10s"
    assert format_duration(70) == "0h 1m 10s"
    assert format_duration(3661) == "1h 1m 1s"


def test_get_total_duration():
    ride_data = {
        "segments": [
            {"status": "moving", "seconds": 3.0},
            {"status": "stopped", "seconds": 7.0},
        ]
    }

    assert get_total_duration(ride_data) == 10.0


def test_get_history_summary():
    rides = [
        {
            "segments": [
                {"status": "moving", "seconds": 3.0},
                {"status": "stopped", "seconds": 7.0},
            ],
            "total": 0.29,
        },
        {
            "segments": [
                {"status": "stopped", "seconds": 10.0},
            ],
            "total": 0.20,
        },
    ]

    summary = get_history_summary(rides)

    assert summary["total_rides"] == 2
    assert summary["total_duration"] == 20.0
    assert summary["total_amount"] == 0.49