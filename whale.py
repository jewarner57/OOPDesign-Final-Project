from fauna import Fauna
from breathemixin import BreatheMixin
import pygame


class Whale(Fauna, BreatheMixin):
    def display(self, screen):
        """displays the whale using pygame"""
        pygame.draw.circle(screen, (0, 0, 255), [self.x, self.y], self.size)
        self.surface()

    def eat(self):
        """Eat the food in the tank"""
        pass
