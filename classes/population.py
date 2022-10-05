# import sys
# sys.path.insert(0,"..")

# import os
# import sys
# sys.path.insert(1, os.getcwd())

from classes.individual import Individual
from classes.enums import Time, Faculty, Room, Course
from rich.console import Console
from rich.table import Table

class Population:
    def __init__(self, seed):
        self.size = seed["initial_population"]

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
        table.add_column("Individual", justify="right", style="cyan", no_wrap=True)
        table.add_column("Fitness", justify="right", style="magenta")
        
        for course in Course:
            table.add_column(course.name, justify="right", style="green")

        i = 1
        for individual in self.individuals:
            # table.add_row("Individual " + str(i), str(individual.get_fitness()))
            table.add_row(str(i), 
                str(individual.get_fitness()), 
                str(individual.course_list[0]), 
                str(individual.course_list[1]), 
                str(individual.course_list[2]), 
                str(individual.course_list[3]), 
                str(individual.course_list[4]), 
                str(individual.course_list[5]), 
                str(individual.course_list[6]), 
                str(individual.course_list[7]), 
                str(individual.course_list[8]), 
                str(individual.course_list[9]))
            i += 1

        console.print(table)
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