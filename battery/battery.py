from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def needs_service():
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date = None, current_date = None):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    @abstractmethod
    def needs_service(self):
        pass

class NubbinBattery(Battery):
    def __init__(self, last_service_date = None, current_date = None):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    @abstractmethod
    def needs_service(self):
        pass