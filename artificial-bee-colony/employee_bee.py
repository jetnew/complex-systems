import numpy as np

from artificial_bee import ArtificialBee

class EmployeeBee(ArtificialBee):

    def explore(self, max_trials):
        if self.trial <= max_trials:
            component = np.random.choice(self.pos)
            phi = np.random.uniform(low=-1, high=1, size=len(self.pos))
            n_pos = self.pos + (self.pos - component) * phi
            n_pos = self.evaluate_boundaries(n_pos)
            n_fitness = self.obj_function.evaluate(n_pos)
            self.update_bee(n_pos, n_fitness)

    def get_fitness(self):
        return 1 / (1 + self.fitness) if self.fitness >= 0 else 1 + np.abs(self.fitness)

    def compute_prob(self, max_fitness):
        self.prob = self.get_fitness() / max_fitness