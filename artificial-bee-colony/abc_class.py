import numpy as np
from copy import deepcopy
from employee_bee import EmployeeBee
from onlooker_bee import OnLookerBee

class ABC:
    def __init__(self, obj_function, colony_size=30, n_iter=5000, max_trials=100):
        self.colony_size = colony_size
        self.obj_function = obj_function

        self.n_iter = n_iter
        self.max_trials = max_trials

        self.optimal_solution = None
        self.optimality_tracking = []

    def __reset_algorithm(self):
        self.optimal_solution = None
        self.optimality_tracking = []

    def __update_optimality_tracking(self):
        self.optimality_tracking.append(self.optimal_solution.fitness)

    def __update_optimal_solution(self):
        n_optimal_solution = \
            min(self.onlokeer_bees + self.employee_bees,
                key=lambda bee: bee.fitness)
        if not self.optimal_solution:
            self.optimal_solution = deepcopy(n_optimal_solution)
        else:
            if n_optimal_solution.fitness < self.optimal_solution.fitness:
                self.optimal_solution = deepcopy(n_optimal_solution)

    def __initialize_employees(self):
        self.employee_bees = []
        for itr in range(self.colony_size // 2):
            self.employee_bees.append(EmployeeBee(self.obj_function))

    def __initialize_onlookers(self):
        self.onlokeer_bees = []
        for itr in range(self.colony_size // 2):
            self.onlokeer_bees.append(OnLookerBee(self.obj_function))

    def __employee_bees_phase(self):
        map(lambda bee: bee.explore(self.max_trials), self.employee_bees)

    def __calculate_probabilities(self):
        sum_fitness = sum(map(lambda bee: bee.get_fitness(), self.employee_bees))
        map(lambda bee: bee.compute_prob(sum_fitness), self.employee_bees)

    def __select_best_food_sources(self):
        self.best_food_sources =\
            filter(lambda bee: bee.prob > np.random.uniform(low=0, high=1),
                   self.employee_bees)
        while not self.best_food_sources:
            self.best_food_sources = \
                filter(lambda bee: bee.prob > np.random.uniform(low=0, high=1),
                       self.employee_bees)

    def __onlooker_bees_phase(self):
        map(lambda bee: bee.onlook(self.best_food_sources, self.max_trials),
            self.onlokeer_bees)

    def __scout_bees_phase(self):
        map(lambda bee: bee.reset_bee(self.max_trials),
            self.onlokeer_bees + self.employee_bees)

    def optimize(self):
        self.__reset_algorithm()
        self.__initialize_employees()
        self.__initialize_onlookers()
        for itr in range(self.n_iter):
            self.__employee_bees_phase()
            self.__update_optimal_solution()

            self.__calculate_probabilities()
            self.__select_best_food_sources()

            self.__onlooker_bees_phase()
            self.__scout_bees_phase()

            self.__update_optimal_solution()
            self.__update_optimality_tracking()
            print("iter: {} = cost: {}"
                  .format(itr, "%04.03e" % self.optimal_solution.fitness))