import unittest
from datetime import datetime

from battery.battery import SpindlerBattery, NubbinBattery
from engine.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from tires.tires import Carrigan, Octoprime

class TestBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date=last_service_date, current_date=today)
        self.assertFalse(battery.needs_service())
    
    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = NubbinBattery(last_service_date=last_service_date, current_date=today)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = NubbinBattery(last_service_date=last_service_date, current_date=today)
        self.assertFalse(battery.needs_service())


class TestEngine(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30_001
        last_service_mileage = 0

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 30_000
        last_service_mileage = 0

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
    
    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60_001
        last_service_mileage = 0

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 60_000
        last_service_mileage = 0

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_on=True)
        self.assertTrue(engine.needs_service())
    
    def test_sternman_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.needs_service())

class TestTires(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        sample = [0.0, 0.1, 0.9, 0.8]
        tires = Carrigan(sample)
        self.assertTrue(tires.needs_service())

    def test_carrigan_should_not_be_serviced(self):
        sample = [0.1, 0.1, 0.1, 0.1]
        tires = Carrigan(sample)
        self.assertFalse(tires.needs_service())
    
    def test_octoprime_should_be_serviced(self):
        sample = [0, 1, 2, 3]
        tires = Octoprime(sample)
        self.assertTrue(tires.needs_service())

    def test_octoprime_should_not_be_serviced(self):
        sample = [1, 0, 1, 0]
        tires = Octoprime(sample)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
