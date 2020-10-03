from fish import Fish
from whale import Whale
from coral import Coral
from algae import Algae
from random import randint


class Tank:
    def __init__(self):
        self.__fish = []
        self.__plants = []

    def display_tank(self, screen):
        """Displays each fish and plant in the tank"""
        for fish in self.__fish:
            fish.display(screen)
            fish.move(screen)

        for plant in self.__plants:
            plant.display(screen)
            plant.grow()

    def feed_tank(self):
        """Feed the fish in the tank"""
        for fish in self.__fish:
            fish.eat()

    def fill_tank(self, screen):
        """Add fish and plants to the tank"""

        width, height = screen.get_size()

        for _ in range(1, 3):
            self.__fish.append(Fish("Clownfish", 20, randint(1, 5), randint(1, 5), randint(
                100, width-100), randint(height-300, height-100)))

        for _ in range(1, 3):
            self.__fish.append(Whale(
                "Humpback", 40, 3, 3, randint(100, width-100), randint(height-300, height-100)))

        for _ in range(1, 3):
            self.__plants.append(Coral("Coral", 20,
                                       5, randint(0, width), height))

        for _ in range(1, 3):
            self.__plants.append(
                Algae("Seaweed", 20, 5, randint(0, width), height))
