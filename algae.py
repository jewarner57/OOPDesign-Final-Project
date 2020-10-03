from flora import Flora
import pygame


class Algae(Flora):
    def display(self, screen):
        """Display the algae plant"""
        pygame.draw.circle(screen, (0, 255, 0), [self.x, self.y], self.size)
