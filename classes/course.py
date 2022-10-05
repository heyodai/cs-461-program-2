class Course:
    def __init__(self, name, time_slot, room, instructor):
        self.name = name
        self.time_slot = time_slot
        self.room = room
        self.instructor = instructor

    def __str__(self):
        return str(self.time_slot) + " " + str(self.room) + " " + str(self.instructor)