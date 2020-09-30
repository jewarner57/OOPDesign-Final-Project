from abc import ABC, abstractmethod
from organism import Organism
from math import floor


class Flora(Organism, ABC):
    def __init__(self, name, size, growSpeed, x=100, y=100):
        super().__init__(name, size, x=x, y=y)
        self.__growSpeed = growSpeed

    def grow(self):
        """Increase size of plant after a time interval"""
        if floor(self.getAge()) % self.__growSpeed == 0:
            self.size += 0.1
