from abc import ABC, abstractmethod

class logAppender(ABC):
    @abstractmethod
    def append(self, message):
        pass