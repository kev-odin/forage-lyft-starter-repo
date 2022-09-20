from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needs_service():
        pass

class Carrigan(Tire):
    def __init__(self, tire_tread):
        self.tread = tire_tread
        
    def needs_service(self):
        for tire in self.tread:
            if tire >= 0.9:
                return True
        return False

class Octoprime(Tire):
    def __init__(self, tire_tread):
        self.tread = tire_tread
    
    def needs_service(self):
        return sum(self.tread) >= 3.0
