from pygame import time, draw
from random import randint


class Bubble:
    def __init__(self, x, y, size):
        self.x = x + randint(-10, 10)
        self.y = y
        self.__size = size
        self.__speed = 1

    def display(self, screen):
        """draws the bubble at it's location"""
        draw.circle(screen, (255, 255, 255), [
                    self.x, self.y], self.__size, width=5)

        if self.__speed <= 8:
            self.__speed += randint(0, 2)

        self.y -= self.__speed
