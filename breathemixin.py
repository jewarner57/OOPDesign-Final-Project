from bubble import Bubble


class BreatheMixin():
    def breatheAir(self):
        """Make the whale swim to the surface to get air"""
        if self.ySpeed > 0 and int(self.getAge()) % 5 == 0:
            self.ySpeed *= -1

    def breatheWater(self, screen):
        """Make the fish breathe water and make bubbles"""
        for bubble in self.bubbles:
            bubble.display(screen)
            if bubble.y < 0:
                self.bubbles.remove(bubble)

        if self.getAge() % 5 < 0.2 and len(self.bubbles) < 2:
            self.bubbles.append(Bubble(self.x, self.y, self.size/2))
