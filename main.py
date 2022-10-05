import sys
sys.path.insert(0,"..")

from classes.population import Population

def main():
    pop = Population(10)
    pop.initialize()

    while(True):
        pop.list()

        pop.compute_fitness()
        pop.remove_weakest()

        pop.create_offspring()
        pop.mutate()

        pop.generation += 1
        if (pop.has_converged()):
            break

SEED = {
    "initial_population": 10,
    "num_offspring": 2,
    "num_mutations": 1
}

main()