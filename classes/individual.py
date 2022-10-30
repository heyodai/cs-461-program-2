import random
import classes.enums as enums
from classes.course import Course


class Individual:
    """
    TODO: verify that this is correct

    An individual is a collection of courses (i.e. genomes).

    Attributes:
        course_list (list): A list of courses.
        fitness (int): The fitness of the individual.

    Methods:
        randomize: Randomizes the individual's course list.
        compute_fitness: Returns the fitness of the individual.
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
            time_slot =  enums.Time( random.randint(1, 6) )
            room = enums.Room( random.randint(1, 9) )
            instructor = enums.Faculty( random.randint(1, 10) )

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

            """
            Assign reference variables for certain courses:
            - CS101A
            - CS101B
            - CS191A
            - CS191B

            This is necessary so that we can check for conflicts between these courses later on.
            """
            if name == enums.Course.CS101A:
                self.cs101a = course
            elif name == enums.Course.CS101B:
                self.cs101b = course
            elif name == enums.Course.CS191A:
                self.cs191a = course
            elif name == enums.Course.CS191B:
                self.cs191b = course

    def add_parents(self, parent1, parent2):
        """
        This method adds the parents' courses to the individual's course list.

        Given two parents, randomly select between each parent for courses until the course list is full.

        Args:
            parent1 (Individual): The first parent.
            parent2 (Individual): The second parent.
        """
        for i in range(0, 11):
            # get a random course from one of the parents
            course = random.choice([parent1.course_list[i], parent2.course_list[i]])
            self.course_list.append(course)

    def compute_fitness(self):
        self.fitness = 0 # reset from previous fitness computation

        filled_room_and_time_slots = []
        instructor_load = {
            "GLADBACH": 0,
            "GHARIBI": 0,
            "HARE": 0,
            "ZEIN_EL_DIN": 0,
            "ZAMAN": 0,
            "NAIT_ABDESSELAM": 0,
            "SONG": 0,
            "SHAH": 0,
            "XU": 0,
            "UDDIN": 0
        }
        instructor_room_time_mappping = {
            "GLADBACH": [],
            "GHARIBI": [],
            "HARE": [],
            "ZEIN_EL_DIN": [],
            "ZAMAN": [],
            "NAIT_ABDESSELAM": [],
            "SONG": [],
            "SHAH": [],
            "XU": [],
            "UDDIN": []
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
            Course-Specific Constraints (part 1)

            The 2 sections of CS 101 are more than 4 hours apart: + 0.5
            Both sections of CS 101 are in the same time slot: -0.5
            The 2 sections of CS 191 are more than 4 hours apart: + 0.5
            Both sections of CS 191 are in the same time slot: -0.5
            """
            if course.name == enums.Course.CS101B:
                if course.time_slot.value - self.cs101a.time_slot.value > 4:
                    self.fitness += 0.5
                if course.time_slot == self.cs101a.time_slot:
                    self.fitness -= 0.5
            elif course.name == enums.Course.CS191B:
                if course.time_slot.value - self.cs191a.time_slot.value > 4:
                    self.fitness += 0.5
                if course.time_slot == self.cs191a.time_slot:
                    self.fitness -= 0.5

            """
            Course-Specific Constraints (part 2)

            A section of CS 191 and a section of CS 101 are taught in consecutive time slots (e.g., 10 AM & 11 AM): 
            +0.5
            
            In this case only (consecutive time slots), one of the classes is in Bloch or Katz, and the other 
            isn’t: -0.4
            
            It’s fine if neither is in one of those buildings, of course; we just want to avoid having consecutive 
            classes being widely separated. Both on the quad (any combination of FH, MNLC, Haag, Royall) is fine, 
            or one class in one of the ‘distant’ buildings and the other on the quad.     
            """
            if self.cs101a.time_slot.value in [self.cs191a.time_slot.value - 1, self.cs191a.time_slot.value + 1, self.cs191b.time_slot.value - 1, self.cs191b.time_slot.value + 1]:
                self.fitness += 0.5
                if (self.cs101a.room.name == "Katz 003" or self.cs101a.room.name == "Bloch 119"):
                    if self.cs101a.room.name not in ["FH 216", "FH 310", "Haag 201", "Haag 301", "Royall 201", "Royall 206", "MNLC 325"]:
                        self.fitness -= 0.4
                
            if self.cs101b.time_slot.value in [self.cs191a.time_slot.value - 1, self.cs191a.time_slot.value + 1, self.cs191b.time_slot.value - 1, self.cs191b.time_slot.value + 1]:
                self.fitness += 0.5
                if (self.cs101b.room.name == "Katz 003" or self.cs101b.room.name == "Bloch 119"):
                    if self.cs101b.room.name not in ["FH 216", "FH 310", "Haag 201", "Haag 301", "Royall 201", "Royall 206", "MNLC 325"]:
                        self.fitness -= 0.4

            if self.cs191a.time_slot.value in [self.cs101a.time_slot.value - 1, self.cs101a.time_slot.value + 1, self.cs101b.time_slot.value - 1, self.cs101b.time_slot.value + 1]:
                self.fitness += 0.5
                if (self.cs191a.room.name == "Katz 003" or self.cs191a.room.name == "Bloch 119"):
                    if self.cs191a.room.name not in ["FH 216", "FH 310", "Haag 201", "Haag 301", "Royall 201", "Royall 206", "MNLC 325"]:
                        self.fitness -= 0.4

            if self.cs191b.time_slot.value in [self.cs101a.time_slot.value - 1, self.cs101a.time_slot.value + 1, self.cs101b.time_slot.value - 1, self.cs101b.time_slot.value + 1]:
                self.fitness += 0.5
                if (self.cs191b.room.name == "Katz 003" or self.cs191b.room.name == "Bloch 119"):
                    if self.cs191b.room.name not in ["FH 216", "FH 310", "Haag 201", "Haag 301", "Royall 201", "Royall 206", "MNLC 325"]:
                        self.fitness -= 0.4

            """
            Course-Specific Constraints (part 3)
 s
            A section of CS 191 and a section of CS 101 are taught separated by 1 hour (e.g., 10 AM & 12:00 Noon): + 0.25
            """
            if self.cs101a.time_slot.value in [self.cs191a.time_slot.value - 2, self.cs191a.time_slot.value + 2, self.cs191b.time_slot.value - 2, self.cs191b.time_slot.value + 2]:
                self.fitness += 0.25

            if self.cs101b.time_slot.value in [self.cs191a.time_slot.value - 2, self.cs191a.time_slot.value + 2, self.cs191b.time_slot.value - 2, self.cs191b.time_slot.value + 2]:
                self.fitness += 0.25

            if self.cs191a.time_slot.value in [self.cs101a.time_slot.value - 2, self.cs101a.time_slot.value + 2, self.cs101b.time_slot.value - 2, self.cs101b.time_slot.value + 2]:
                self.fitness += 0.25

            if self.cs191b.time_slot.value in [self.cs101a.time_slot.value - 2, self.cs101a.time_slot.value + 2, self.cs101b.time_slot.value - 2, self.cs101b.time_slot.value + 2]:
                self.fitness += 0.25

            """
            Course-Specific Constraints (part 4)

            A section of CS 191 and a section of CS 101 are taught in the same time slot: -0.25
            """
            if self.cs101a.time_slot.value in [self.cs191a.time_slot, self.cs191b.time_slot]:
                self.fitness -= 0.25

            if self.cs101b.time_slot.value in [self.cs191a.time_slot, self.cs191b.time_slot]:
                self.fitness -= 0.25

            if self.cs191a.time_slot.value in [self.cs101a.time_slot, self.cs101b.time_slot]:
                self.fitness -= 0.25

            if self.cs191b.time_slot.value in [self.cs101a.time_slot, self.cs101b.time_slot]:
                self.fitness -= 0.25


        """
        Instructor Load (part 2)
        
        Instructor is scheduled to teach more than 4 classes total: -0.5
        Instructor is scheduled to teach 1 or 2 classes: -0.4
            Exception: Dr. Xu is division chair and has other demands on his time. No penalty if he’s only teaching
            1 or 2 courses (or isn’t on the schedule at all). 
        """
        for name, load in instructor_load.items():
            if load > 4:
                self.fitness -= 0.5
            elif load <= 2 and name != "XU":
                self.fitness -= 0.4

        # rounding is necessary to avoid weird floating points
        self.fitness = round(self.fitness, 2)

    def __str__(self):
        output = ""
        for course in self.course_list:
            output += str(course)

        return output
