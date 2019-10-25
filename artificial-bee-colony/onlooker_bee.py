import numpy as np
from artificial_bee import ArtificialBee

class OnLookerBee(ArtificialBee):

    def onlook(self, best_food_sources, max_trials):
        candidate = np.random.choice(best_food_sources)
        self.__exploit(candidate.pos, candidate.fitness, max_trials)

    def __exploit(self, candidate, fitness, max_trials):
        if self.trial <= max_trials:
            component = np.random.choice(candidate)
            phi = np.random.uniform(low=-1, high=1, size=len(candidate))
            n_pos = candidate + (candidate - component) * phi
            n_pos = self.evaluate_boundaries(n_pos)
            n_fitness = self.obj_function.evaluate(n_pos)

            if n_fitness <= fitness:
                self.pos = n_pos
                self.fitness = n_fitness
                self.trial = 0
            else:
                self.trial += 1