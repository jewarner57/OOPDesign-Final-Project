from abc import ABC, abstractmethod
from pygame import time


class Organism(ABC):
    def __init__(self, name, size, x=100, y=100):
        self.name = name
        self.size = size
        self.x = x
        self.y = y

    def getAge(self):
        return time.get_ticks()/1000

    @abstractmethod
    def display(self, screen):
        """Display the object at x, y"""
        pass
