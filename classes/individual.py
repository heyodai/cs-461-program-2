import random
import classes.enums as enums
from classes.course import Course

class Individual:
    def __init__(self):
        self.course_list = []

    def randomize(self):
        for i in range(1, 11):
            # random ints map to enums
            name = enums.Course(i)
            time_slot = random.randint(1, 6)
            room = random.randint(1, 9)
            instructor = random.randint(1, 10)

            course = Course(name, time_slot, room, instructor)
            self.course_list.append(course)

    def get_fitness():
        pass

    def __str__(self):
        output = ""
        for course in self.course_list:
            output += str(course)
            
        return output