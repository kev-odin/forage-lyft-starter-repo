from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service():
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage = 0, current_mileage = 0):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30_000


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage = 0, current_mileage = 0):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60_000


class SternmanEngine(Engine):
    def __init__(self, warning_light_on = False):
        self.warning_light_on = warning_light_on
    
    def needs_service(self):
        return self.warning_light_on


