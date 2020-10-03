from abc import ABC, abstractmethod
from organism import Organism


class Fauna(Organism, ABC):
    def __init__(self, name, size, xSpeed, ySpeed, x, y):
        super().__init__(name, size, x, y)
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    @abstractmethod
    def eat(self):
        """Eat the food in the tank"""
        pass

    def move(self, screen):
        """Move around the tank"""
        width, height = screen.get_size()

        self.x += self.xSpeed
        self.y += self.ySpeed

        if self.x > width or self.x < 0:
            self.xSpeed *= -1
        if self.y > height or self.y < 0:
            self.ySpeed *= -1
