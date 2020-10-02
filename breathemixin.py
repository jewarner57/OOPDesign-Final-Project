from bubble import Bubble


class BreatheMixin():
    def surface(self):
        """Make the whale swim to the surface to get air"""
        if self.ySpeed > 0 and int(self.getAge()) % 5 == 0:
            self.ySpeed *= -1
