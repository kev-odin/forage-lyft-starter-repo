from engine.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery.battery import SpindlerBattery, NubbinBattery
from tires.tires import Carrigan, Octoprime
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self.car_engine = engine
        self.car_battery = battery
        self.tires = tire

    def needs_service(self):
        return self.car_battery.needs_service() or self.car_engine.needs_service() or self.tires.need_service()



class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tread_life):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = Carrigan(tread_life)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tread_life):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = Carrigan(tread_life)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tread_life):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = Octoprime(tread_life)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tread_life):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = Carrigan(tread_life)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tread_life):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = Carrigan(tread_life)
        car = Car(engine, battery, tire)
        return car


