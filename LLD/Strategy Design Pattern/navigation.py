from abc import ABC, abstractmethod


class routeStrategy(ABC):
    @abstractmethod
    def calculateTime(self, distance):
        pass

class carStrategy(routeStrategy):
    def calculateTime(self, distance):
        speed = 60
        return distance/speed

class bikeStrategy(routeStrategy):
    def calculateTime(self, distance):
        speed = 40
        return distance/speed
    
class publicStrategy(routeStrategy):
    def calculateTime(self, distance):
        speed = 30
        waitTime = 0.25
        return distance/speed + waitTime
    
class navigatorContext:
    def __init__(self, strategy:routeStrategy):
        self.strategy = strategy
    def setStrategy(self, strategy:routeStrategy):
        self.strategy = strategy
    def calculateTime(self, distance):
        return self.strategy.calculateTime(distance)