from pufferfish import Pufferfish
from humpbackwhale import Humpbackwhale
from coral import Coral
from seaweed import Seaweed
from random import randint


class Tank:
    def __init__(self):
        self._fish = []
        self._plants = []

    def display_tank(self, screen):
        """Displays each fish and plant in the tank"""
        for fish in self._fish:
            fish.display(screen)
            fish.move(screen)

        for plant in self._plants:
            plant.display(screen)
            plant.grow()

    def feed_tank(self):
        """Feed the fish in the tank"""
        for fish in self._fish:
            fish.eat()

    def fill_tank(self, screen):
        """Add fish and plants to the tank"""

        width, height = screen.get_size()

        for _ in range(1, 3):
            self._fish.append(Pufferfish("Puffer", 20, 5, 2))

        for _ in range(1, 3):
            self._fish.append(Humpbackwhale(
                "Humpback", 40, 3, 3, randint(100, width-100), randint(height-300, height-100)))

        for _ in range(1, 3):
            self._plants.append(Coral("Coral", 20,
                                      5, randint(0, width), height))

        for _ in range(1, 3):
            self._plants.append(
                Seaweed("Seaweed", 20, 5, randint(0, width), height))
