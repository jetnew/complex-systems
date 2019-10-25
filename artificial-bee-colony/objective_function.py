import numpy as np

from scipy import optimize
from deap.benchmarks import schwefel


class ObjectiveFunction(object):

    def __init__(self, name, dim, minf, maxf):
        self.name = name
        self.dim = dim
        self.minf = minf
        self.maxf = maxf

    def sample(self):
        return np.random.uniform(low=self.minf, high=self.maxf, size=self.dim)

    def custom_sample(self):
        return np.repeat(self.minf, repeats=self.dim) \
               + np.random.uniform(low=0, high=1, size=self.dim) *\
               np.repeat(self.maxf - self.minf, repeats=self.dim)

    def evaluate(self, x):
        pass

class Sphere(ObjectiveFunction):

    def __init__(self, dim):
        super(Sphere, self).__init__('Sphere', dim, -100.0, 100.0)

    def evaluate(self, x):
        return sum(np.power(x, 2))


class Rosenbrock(ObjectiveFunction):

    def __init__(self, dim):
        super(Rosenbrock, self).__init__('Rosenbrock', dim, -30.0, 30.0)

    def evaluate(self, x):
        return optimize.rosen(x)


class Rastrigin(ObjectiveFunction):

    def __init__(self, dim):
        super(Rastrigin, self).__init__('Rastrigin', dim, -5.12, 5.12)

    def evaluate(self, x):
        return 10 * len(x)\
               + np.sum(np.power(x, 2) - 10 * np.cos(2 * np.pi * np.array(x)))


class Schwefel(ObjectiveFunction):

    def __init__(self, dim):
        super(Schwefel, self).__init__('Schwefel', dim, -500.0, 500.0)

    def evaluate(self, x):
        return schwefel(x)[0]