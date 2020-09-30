from pygame import time, draw
from random import randint


class Bubble:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.lifeLength = 5
        self.speed = 1
        self.deathSecond = (time.get_ticks()/1000) + self.lifeLength

    def display(self, screen):
        draw.circle(screen, (255, 255, 255), [self.x, self.y], self.size)

        if self.speed <= 8:
            self.speed += randint(0, 2)

        self.y -= self.speed
