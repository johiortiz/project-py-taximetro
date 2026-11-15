import unittest
from unittest.mock import patch

from src.ride import Ride


class TestRide(unittest.TestCase):
    def setUp(self):
        self.fares = {
            "stopped": 0.02,
            "moving": 0.05,
        }

    def test_ride_starts_stopped(self):
        ride = Ride(self.fares)

        ride.start()

        self.assertEqual(ride.status, "stopped")
        self.assertFalse(ride.finished)
        self.assertEqual(ride.segments, [])

    def test_ten_seconds_stopped_costs_0_20(self):
        with patch("src.ride.time.monotonic", side_effect=[10, 20]):
            ride = Ride(self.fares)
            ride.start()
            total = ride.finish()

        self.assertEqual(total, 0.20)

    def test_mixed_ride_costs_0_70(self):
        with patch("src.ride.time.monotonic", side_effect=[10, 20, 30, 40]):
            ride = Ride(self.fares)
            ride.start()
            ride.set_status("moving")
            total = ride.finish()

        self.assertEqual(total, 0.70)

if __name__ == "__main__":
    unittest.main()