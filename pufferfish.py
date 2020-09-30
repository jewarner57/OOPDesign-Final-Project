from fauna import Fauna
import pygame
from bubble import Bubble
from random import randint


class Pufferfish(Fauna):
    def puff_up(self):
        """Temporarily increase the fish' size."""

    def display(self, screen):
        pygame.draw.circle(screen, (245, 209, 65), [self.x, self.y], self.size)

        for bubble in self.bubbles:
            bubble.display(screen)
            if (pygame.time.get_ticks()/1000) > bubble.deathSecond:
                del bubble

    def eat(self):
        """Eat the food in the tank"""
        for i in range(0, 3):
            self.bubbles.append(
                Bubble(self.x+randint(-self.size, self.size), self.y, self.size/2))
        pass
