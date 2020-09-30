from fauna import Fauna
from breathemixin import BreatheMixin
import pygame


class Humpbackwhale(Fauna, BreatheMixin):
    def display(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), [self.x, self.y], self.size)
        self.breath_air()

    def eat(self):
        """Eat the food in the tank"""
        pass
