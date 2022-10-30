import random
from classes.individual import Individual
from classes.enums import Time, Faculty, Room, Course #TODO: can any of these be removed?
from rich.console import Console
from rich.table import Table

class Population:
    """
    TODO: verify that this is correct

    A population is a collection of individuals.

    Attributes:
        size (int): The number of individuals in the population.
        individuals (list): A list of individuals.
        generation (int): The generation number.

    Methods:
        initialize: Randomly generate individuals.
        print: Print the current population data.
        compute_fitness: Compute the fitness of each individual.
        remove_weakest: Remove the weakest individuals.
        create_offspring: Create offspring from the remaining individuals.
        mutate: Mutate the offspring.
        has_converged: Check if the population has converged.
    """
    def __init__(self, seed):
        self.size = seed["initial_population"]
        self.num_offspring = seed["num_offspring"]
        self.num_mutations = seed["num_mutations"]
        self.num_generations = seed["num_generations"]

        self.individuals = []
        self.generation = 1

    def initialize(self):
        for i in range(self.size):
            individual = Individual()
            individual.randomize()
            self.individuals.append(individual)

    def print(self):
        print("Generation: " + str(self.generation))

        console = Console()
        table = Table(show_header=True, header_style="bold magenta")

        table.add_column("#", justify="right", style="cyan", width=2)
        table.add_column("Fitness", justify="right", style="magenta", width=6)
        for course in Course:
            table.add_column(course.name, justify="left", style="green")

        i = 1
        for individual in self.individuals:
            table.add_row(str(i), 
                str(individual.fitness),
                str(individual.course_list[0]), 
                str(individual.course_list[1]), 
                str(individual.course_list[2]), 
                str(individual.course_list[3]), 
                str(individual.course_list[4]), 
                str(individual.course_list[5]), 
                str(individual.course_list[6]), 
                str(individual.course_list[7]), 
                str(individual.course_list[8]), 
                str(individual.course_list[9]),
                str(individual.course_list[10]))
            i += 1

        console.print(table)
        print("")

    def compute_fitness(self):
        for individual in self.individuals:
            individual.compute_fitness()

    def remove_weakest(self):
        """
        Remove weakest individuals from the population.

        To do so, we sort the individuals by fitness, and remove the last half.
        """
        self.individuals.sort(key=lambda x: x.fitness)
        self.individuals = self.individuals[-int(self.size/2):]

    def create_offspring(self):
        """
        Create offspring from the remaining individuals.

        To do so, we randomly select two individuals from the population, and
        create two offspring from them.

        The offspring are added to the population.
        """
        # pass
        for i in range(self.num_offspring):
            # randomly select two individuals
            parent1 = self.individuals[random.randint(0, len(self.individuals)-1)]
            parent2 = self.individuals[random.randint(0, len(self.individuals)-1)]

            # create two offspring from them
            # offspring1 = parent1.crossover(parent2)
            # offspring2 = parent2.crossover(parent1)
            offspring1 = parent1
            offspring2 = parent2

            # add the offspring to the population
            self.individuals.append(offspring1)
            self.individuals.append(offspring2)

    def mutate(self):
        """
        Randomly change a course or two for each individual.
        """
        for individual in self.individuals:
            for i in range(random.choice(range(self.num_mutations+1))):
                # create a course randomly
                course_list_length = len(individual.course_list)
                # course = individual.course_list[(random.choice(course_list_length))]
                course = individual.course_list[random.randint(0, course_list_length-1)]

                # remove a random course from the individual
                # individual.course_list.remove(random.choice(individual.course_list))
                individual.course_list.pop()

                # add the new course to the individual
                individual.course_list.append(course)

    def has_converged(self):
        return self.generation > self.num_generations