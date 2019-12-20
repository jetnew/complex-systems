import random


class Blob:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.replicate_chance = 0.40  # 0.20
        self.die_chance = 0.30  # 0.125
        self.mutate_chance = 0.01  # 0.001
        self.mutate_value = 0.4

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
            world.create_blob(new_x, new_y, (
                self.val[0] + self._mutate(),
                self.val[1] + self._mutate(),
                self.val[2] + self._mutate()))

    def die(self, world):
        world.delete_blob(self.x, self.y)

    def _mutate(self):
        if random.random() < self.mutate_chance:
            if random.random() < 0.50:
                return self.mutate_value
            else:
                return -self.mutate_value
        else:
            return 0

    def next(self, world):
        if random.random() < self.replicate_chance:
            self.replicate(world)
        if random.random() < self.die_chance:
            self.die(world)