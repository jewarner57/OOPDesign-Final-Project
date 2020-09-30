from flora import Flora
import pygame


class Seaweed(Flora):

    def display(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), [self.x, self.y], self.size)
