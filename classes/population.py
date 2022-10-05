# import sys
# sys.path.insert(0,"..")

# import os
# import sys
# sys.path.insert(1, os.getcwd())

from classes.individual import Individual

class Population:
    def __init__(self, size):
        self.size = size

        self.individuals = []
        self.generation = 1

    def initialize(self):
        for i in range(self.size):
            individual = Individual()
            individual.randomize()
            self.individuals.append(individual)

    def list(self):
        print("Generation: " + str(self.generation))
        
        i = 1
        for individual in self.individuals:
            print("Individual " + str(i) + ": " + str(individual))
            i += 1

        print("")

    def compute_fitness(self):
        pass

    def remove_weakest(self):
        pass

    def create_offspring(self):
        pass

    def mutate(self):
        pass

    def has_converged(self):
        return self.generation > 2