class Student:

    def __init__(self, school):
        self.school = school
        self.health = 80

        if school == "high":
            self.stress = 100
            self.smarts = 70
            self.happiness = 130
            self.maxes = {
                "health": 100,
                "stress": 200,
                "smarts": 100,
                "happiness": 150,
            }
        else:
            self.stress = 60
            self.smarts = 130
            self.happiness = 70
            self.maxes = {
                "health": 100,
                "stress": 100,
                "smarts": 150,
                "happiness": 100,
            }

    def perform_task(self, task):
        self.health += task.health
        self.stress_points -= task.stress
        self.smarts += task.smarts
        self.happiness += task.happiness



