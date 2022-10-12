class Course:
    """
    A course is a collection of the following attributes:
    - name: string
    - time_slot: Time
    - room: Room
    - instructor: Faculty
    - expected_enrollment: int
    - section: int
    - preferred_instructors: list of Faculty
    - other_instructors: list of Faculty
    """
    def __init__(self, name, time_slot, room, instructor, expected_enrollment, section, preferred_instructors, other_instructors):
        self.name = name
        self.time_slot = time_slot
        self.room = room
        self.instructor = instructor

        self.expected_enrollment = expected_enrollment
        self.section = section
        self.preferred_instructors = preferred_instructors
        self.other_instructors = other_instructors

        self.fitness = 0

    def __str__(self):
        return str(self.time_slot.value) + " " + str(self.room.value) + " " + str(self.instructor.value)