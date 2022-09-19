from abc import ABC, abstractmethod
from datetime import date
from engine.engine import Engine
from battery.battery import Battery
from serviceable import Serviceable


class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):  # type: ignore
        pass
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):  # type: ignore
        pass
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):  # type: ignore
        pass
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):  # type: ignore
        pass
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):  # type: ignore
        pass

class Car(Serviceable):
    def __init__(self, last_service_date):
        self.car_engine = None
        self.car_battery = None

    @abstractmethod
    def needs_service(self):
        pass
