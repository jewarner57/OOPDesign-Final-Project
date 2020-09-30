from flora import Flora
import pygame


class Coral(Flora):

    def display(self, screen):
        pygame.draw.circle(screen, (255, 50, 0), [self.x, self.y], self.size)
        pygame.draw.circle(screen, (255, 50, 0), [
                           self.x, self.y-self.size], self.size)
