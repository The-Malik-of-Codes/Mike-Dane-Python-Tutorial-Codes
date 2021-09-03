class  Student:

    def __init__(self, name, age, major, gpa, is_on_probation):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honour_roll(self):
        if self.gpa >= 4.5:
            return True
        else:
            return False