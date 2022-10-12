import random
import classes.enums as enums
from classes.course import Course


class Individual:
    """
    An individual is a collection of courses (i.e. genomes).

    Attributes:
        course_list (list): A list of courses.
        fitness (int): The fitness of the individual.

    Methods:
        randomize: Randomizes the individual's course list.
        get_fitness: Returns the fitness of the individual.
        __str__: Returns a string representation of the individual.
    """

    def __init__(self):
        self.course_list = []
        self.fitness = 0

    def randomize(self):
        for i in range(1, 12):
            name = enums.Course(i)

            """
            Random ints can be mapped to enums. This is a bit of a hack, but it works.
            """
            time_slot = random.randint(1, 6)
            room = random.randint(1, 9)
            instructor = random.randint(1, 10)

            """
            The unwieldy statement below is due to Python not having a switch statement :/
            """
            if name == enums.Course.CS101A:
                expected_enrollment = 50
                section = "A"
                preferred_instructors = ["Gladbach",
                                         "Gharibi", "Hare", "Zein el Din"]
                other_instructors = ["Zaman", "Nait-Abdesselam"]
            elif name == enums.Course.CS101B:
                expected_enrollment = 50
                section = "B"
                preferred_instructors = ["Gladbach",
                                         "Gharibi", "Hare", "Zein el Din"]
                other_instructors = ["Zaman", "Nait-Abdesselam"]
            elif name == enums.Course.CS191A:
                expected_enrollment = 50
                section = "A"
                preferred_instructors = ["Gladbach",
                                         "Gharibi", "Hare", "Zein el Din"]
                other_instructors = ["Zaman", "Nait-Abdesselam"]
            elif name == enums.Course.CS191B:
                expected_enrollment = 50
                section = "B"
                preferred_instructors = ["Gladbach",
                                         "Gharibi", "Hare", "Zein el Din"]
                other_instructors = ["Zaman", "Nait-Abdesselam"]
            elif name == enums.Course.CS201:
                expected_enrollment = 50
                section = None
                preferred_instructors = [
                    "Gladbach", "Hare", "Zein el Din", "Shah"]
                other_instructors = ["Zaman", "Nait-Abdesselam", "Song"]
            elif name == enums.Course.CS291:
                expected_enrollment = 50
                section = None
                preferred_instructors = [
                    "Gharibi", "Hare", "Zein el Din", "Song"]
                other_instructors = ["Zaman", "Nait-Abdesselam", "Shah", "Xu"]
            elif name == enums.Course.CS303:
                expected_enrollment = 60
                section = None
                preferred_instructors = ["Gladbach", "Zein el Din", "Hare"]
                other_instructors = ["Zaman", "Song", "Shah"]
            elif name == enums.Course.CS304:
                expected_enrollment = 25
                section = None
                preferred_instructors = ["Gladbach", "Hare", "Xu"]
                other_instructors = [
                    "Zaman",
                    "Song",
                    "Shah",
                    "Nait-Abdesselam",
                    "Uddin",
                    "Zein el Din",
                ]
            elif name == enums.Course.CS394:
                expected_enrollment = 20
                section = None
                preferred_instructors = ["Xu", "Song"]
                other_instructors = ["Nait-Abdesselam", "Zein el Din"]
            elif name == enums.Course.CS449:
                expected_enrollment = 60
                section = None
                preferred_instructors = ["Xu", "Song", "Shah"]
                other_instructors = ["Zein el Din", "Uddin"]
            elif name == enums.Course.CS451:
                expected_enrollment = 100
                section = None
                preferred_instructors = ["Xu", "Song", "Shah"]
                other_instructors = ["Zein el Din",
                                     "Uddin", "Nait-Abdesselam", "Hare"]
            else:
                raise ValueError(f"Invalid course name: {name}")

            course = Course(name, time_slot, room, instructor, expected_enrollment,
                            section, preferred_instructors, other_instructors)
            self.course_list.append(course)

    def get_fitness(self):
        filled_room_and_time_slots = []
        instructor_load = {
            "Gladbach": 0,
            "Gharibi": 0,
            "Hare": 0,
            "Zein el Din": 0,
            "Zaman": 0,
            "Nait-Abdesselam": 0,
            "Song": 0,
            "Shah": 0,
            "Xu": 0,
            "Uddin": 0
        }
        instructor_room_time_mappping = {
            "Gladbach": [],
            "Gharibi": [],
            "Hare": [],
            "Zein el Din": [],
            "Zaman": [],
            "Nait-Abdesselam": [],
            "Song": [],
            "Shah": [],
            "Xu": [],
            "Uddin": []
        }

        for course in self.course_list:
            """ 
            Time Slot and Room Constraint

            Class is scheduled at the same time in the same room as another class: -0.5 
            """
            room_time_slot = {
                "room": course.room,
                "time_slot": course.time_slot
            }

            if room_time_slot not in filled_room_and_time_slots:
                filled_room_and_time_slots.append(room_time_slot)
            else:
                self.fitness -= 0.5

            """
            Room Size

            Class is in a room too small for its expected enrollment: -0.5
            Class is in a room with capacity > 3 times expected enrollment: -0.2
            Class is in a room with capacity > 6 times expected enrollment: -0.4
            Otherwise + 0.3
            """
            room_capacities = [
                {"name": "Katz 003", "capacity": 45},
                {"name": "FH 216", "capacity": 30},
                {"name": "Royall 206", "capacity": 75},
                {"name": "Royall 201", "capacity": 50},
                {"name": "FH 310", "capacity": 108},
                {"name": "Haag 201", "capacity": 60},
                {"name": "Haag 301", "capacity": 75},
                {"name": "MNLC 325", "capacity": 450},
                {"name": "Bloch 119", "capacity": 60}
            ]
            for room in room_capacities:
                if room["name"] == course.room.name:
                    if room["capacity"] < course.expected_enrollment:
                        self.fitness -= 0.5
                    elif room["capacity"] > course.expected_enrollment * 3:
                        self.fitness -= 0.2
                    elif room["capacity"] > course.expected_enrollment * 6:
                        self.fitness -= 0.4
                    else:
                        self.fitness += 0.3

            """
            Instructor Preference

            Class is taught by a preferred faculty member: + 0.5
            Class is taught by another faculty member listed for that course: +0.2
            Class is taught by some other faculty: -0.1 
            """
            if course.instructor.name in course.preferred_instructors:
                self.fitness += 0.5
            elif course.instructor.name in course.other_instructors:
                self.fitness += 0.2
            else:
                self.fitness -= 0.1

            """
            Instructor Load (part 1)

            Course instructor is scheduled for only 1 class in this time slot: + 0.2
            Course instructor is scheduled for more than one class at the same time: - 0.2
            """
            instructor_room_time = {
                "instructor": course.instructor.name,
                "room": course.room.name,
                "time_slot": course.time_slot
            }
            if instructor_room_time not in instructor_room_time_mappping[course.instructor.name]:
                instructor_room_time_mappping[course.instructor.name].append(
                    instructor_room_time)
            else:
                self.fitness -= 0.2

            instructor_load[course.instructor.name] += 1

        """
        Instructor Load (part 2)
        
        Instructor is scheduled to teach more than 4 classes total: -0.5
        Instructor is scheduled to teach 1 or 2 classes: -0.4
            Exception: Dr. Xu is division chair and has other demands on his time. No penalty if he’s only teaching 1 or 2 courses (or isn’t on the schedule at all). 
        """
        for instructor in instructor_load:
            if instructor_load[instructor["name"]] > 4:
                self.fitness -= 0.5
            elif instructor_load[instructor["name"]] <= 2 and instructor["name"] != "Xu":
                self.fitness -= 0.4

    def __str__(self):
        output = ""
        for course in self.course_list:
            output += str(course)

        return output
