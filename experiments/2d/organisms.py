from utils import chance
import random
import numpy as np


class Blob:
    def __init__(self, x, y, colour):
        """
        x, y - coordinates
        attrs - attributes:
            - replicate_chance = 0.20
            - die_chance = 0.00
            - die_increment = 0.052
            - mutate_chance = 0.01
            - mutate_value = 0.4
            - colour = (1, 1, 1)
        """
        self.x = x
        self.y = y
        self.replicate_chance = 0.20
        self.die_chance = 0.00
        self.die_increment = 0.052
        self.mutate_chance = 0.01
        self.mutate_value = 0.4
        self.colour = colour
        self.perceive_field = 2

    def replicate(self, world):
        _dx, _dy = random.choice(((-1, -1),
                                  (-1, 0),
                                  (-1, 1),
                                  (0, -1),
                                  (0, 1),
                                  (1, -1),
                                  (1, 0),
                                  (1, 1)))
        new_x = self.x + _dx
        new_y = self.y + _dy

        if 0 <= new_x < world.dimx and 0 <= new_y < world.dimy:
            colour = (
                self.colour[0] + self._mutate(),
                self.colour[1] + self._mutate(),
                self.colour[2] + self._mutate(),
            )
            world.create_blob(new_x, new_y, colour)

    def die(self, world):
        world.delete_blob(self.x, self.y)

    def _mutate(self):
        if chance(self.mutate_chance):
            if chance(0.50):
                return self.mutate_value
            else:
                return -self.mutate_value
        else:
            return 0

    def _get_perceive_field(self, world):
        x1 = self.x - self.perceive_field
        x2 = self.x + self.perceive_field
        y1 = self.y - self.perceive_field
        y2 = self.y + self.perceive_field
        if x1 < 0:
            x1 = 0
        if x2 > world.dimx - 1:
            x2 = world.dimx - 1
        if y1 < 0:
            y1 = 0
        if y2 > world.dimy - 1:
            y2 = world.dimy - 1
        return x1, x2, y1, y2, world.space[x1:x2+1, y1:y2+1]

    def perceive(self, world):
        x1, x2, y1, y2, field = self._get_perceive_field(world)
        self.neighbors = np.count_nonzero(field)
        self.empty = (self.perceive_field * 2 + 1) ** 2 - self.neighbors
        self.like = np.count_nonzero(self.colour)

    def next(self, world):
        self.perceive(world)

        if chance(self.replicate_chance):
            self.replicate(world)
        if chance(self.die_chance):
            self.die(world)
        self.die_chance += self.die_increment