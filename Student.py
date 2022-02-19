class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        if school == "high":
            self.stress_points = 200
        else:
            self.stress_points = 100

    def perform_task(self, task):
        self.stress_points -= task.stress

