# modify sys path so class libraries can be imported
import sys
sys.path.insert(0,"..")

from classes.population import Population

def main():
    pop = Population(SEED)
    pop.initialize()

    while(True):
        pop.print()

        pop.compute_fitness()
        pop.remove_weakest()

        pop.create_offspring()
        pop.mutate()

        pop.generation += 1
        if (pop.has_converged()):
            break

# initialization parameters
SEED = {
    "initial_population": 10,
    "num_offspring": 2,
    "num_mutations": 1,
    "num_generations": 5,
}

main()