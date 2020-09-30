from tank import Tank
import pygame
import sys


class Simulation:
    def __init__(self):
        self.__tank = None
        self.__screen = None
        self.__simAge = 0

    def create_tank(self):
        """Create A Tank Object and Fill it With Creatures"""
        self.__tank = Tank()
        self.__tank.fill_tank(self.__screen)

    def pygame_setup(self):
        """Start pygame and set values for window properties"""
        pygame.init()

        size = width, height = 800, 800
        self.__screen = pygame.display.set_mode(size)

    def run_simulation(self):
        """Run the simulation and draw the tank"""
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.__screen.fill((24, 79, 242))

            self.__tank.display_tank(self.__screen)

            events = pygame.event.get()
            for event in events:
                print(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__tank.feed_tank()

            pygame.display.flip()

        sys.exit()
