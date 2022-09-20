from abc import ABC, abstractmethod
from datetime import datetime


class Battery(ABC):
    @abstractmethod
    def needs_service():
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return self.current_date.year - self.last_service_date.year >= 2

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return self.current_date.year - self.last_service_date.year >= 4
