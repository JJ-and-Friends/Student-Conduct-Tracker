from abc import ABC, abstractmethod

class KarmaStrategy(ABC):
    @abstractmethod
    def execute(self, student):
        pass