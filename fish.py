from fauna import Fauna
from breathemixin import BreatheMixin
import pygame


class Fish(Fauna, BreatheMixin):
    def __init__(self, name, size, xSpeed=5, ySpeed=5, x=100, y=100):
        super().__init__(name, size, xSpeed, ySpeed, x, y)
        self.bubbles = []

    def display(self, screen):
        """displays the fish using pygame"""
        pygame.draw.circle(screen, (255, 165, 0), [self.x, self.y], self.size)
        self.breatheWater(screen)

    def eat(self):
        """Eat the food in the tank"""
