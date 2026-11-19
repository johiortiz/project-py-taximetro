import unittest

from src.taximeter import calculate_total


class TestCalculateTotal(unittest.TestCase):
    def test_calculates_mixed_rides(self):
        segments = [
            {"status": "stopped", "seconds": 20},
            {"status": "moving", "seconds": 30},
        ]
        fares = {
            "stopped": 0.02,
            "moving": 0.05,
        }
        result = calculate_total(segments, fares)
        self.assertEqual(result, 1.9)

    def test_calculate_only_stopped_ride(self):
        segments = [
            {"status": "stopped", "seconds": 60},
        ]
        fares = {
            "stopped": 0.02,
            "moving": 0.05,
        }

        result = calculate_total(segments, fares)

        self.assertEqual(result, 1.2)

    def test_calculates_only_moving_ride(self):
        segments = [
            {"status": "moving", "seconds": 120},
        ]
        fares = {
            "stopped": 0.02,
            "moving": 0.05,
        }

        result = calculate_total(segments, fares)
        self.assertEqual(result, 6.0)

    def test_returns_zero_for_empty_ride(self):
        segments = []
        fares = {
            "stopped": 0.02,
            "moving": 0.05,
        }

        result = calculate_total(segments, fares)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()