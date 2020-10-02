from fauna import Fauna
import pygame


class Fish(Fauna):
    def display(self, screen):
        """displays the fish using pygame"""
        pygame.draw.circle(screen, (255, 165, 0), [self.x, self.y], self.size)

    def eat(self):
        """Eat the food in the tank"""
