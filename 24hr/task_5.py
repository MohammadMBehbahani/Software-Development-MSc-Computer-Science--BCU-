class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        if value < 0 or value > 121:
            return
        else:
            self.age = value
    
    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, value):
        if value != "M" or value != "F":
            return
        else:
            self.gender = value

class FreshStudent(Student):
    def __init__(self, name, age, gender, averageMark, level):
        super().__init__(name, age, gender)
        self.averageMark = averageMark
        self.level = level

    @property
    def averageMark(self):
        return self.averageMark

    @averageMark.setter
    def averageMark(self, value):
        if value < 1 or value < 100:
            return
        else:
            self.averageMark = value

    @property
    def level(self):
        return self.level

    @level.setter
    def level(self, value):
        if value == "UG1" or value == "UG2" or value == "UG3" or value == "UG4":
            return
        else:
            self.level = value


def main():
    s1 = FreshStudent("Robert", 36, "M", 76, "UG1")
    print("Student-Name Age Gender Level Average-Mark")
    print(f"{s1.name} {s1.age} {s1.gender} {s1.level} {s1.averageMark}")

main()