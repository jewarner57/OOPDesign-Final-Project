from flora import Flora
import pygame


class Coral(Flora):
    # although coral is technically an animal it behaves more like a plant
    # which is why I have classified it as one for this program
    def display(self, screen):
        """draws the coral using pygame"""
        pygame.draw.circle(screen, (255, 50, 0), [self.x, self.y], self.size)
        pygame.draw.circle(screen, (255, 50, 0), [
                           self.x, self.y-self.size], self.size)
