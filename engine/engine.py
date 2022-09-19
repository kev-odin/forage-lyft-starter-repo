from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service():
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage = 0, current_mileage = 0):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    @abstractmethod
    def needs_service(self):
        pass


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage = 0, current_mileage = 0):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    @abstractmethod
    def needs_service(self):
        pass


class SternmanEngine(Engine):
    def __init__(self, warning_light_on = False):
        self.warning_light_on = warning_light_on
    
    @abstractmethod
    def needs_service(self):
        pass


