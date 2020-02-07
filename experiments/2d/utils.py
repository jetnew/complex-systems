import random


def chance(r):
    assert 0 <= r <= 1
    return random.random() < r
