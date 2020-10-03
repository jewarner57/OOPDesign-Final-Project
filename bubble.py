from pygame import time, draw
from random import randint


class Bubble:
    def __init__(self, x, y, size):
        self.x = x + randint(-10, 10)
        self.y = y
        self.size = size
        self.lifeLength = 5
        self.speed = 1
        self.deathSecond = (time.get_ticks()/1000) + self.lifeLength

    def display(self, screen):
        """draws the bubble at it's location"""
        draw.circle(screen, (255, 255, 255), [
                    self.x, self.y], self.size, width=5)

        if self.speed <= 8:
            self.speed += randint(0, 2)

        self.y -= self.speed
