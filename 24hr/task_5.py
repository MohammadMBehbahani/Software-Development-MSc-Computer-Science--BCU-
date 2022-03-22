class Student:
    def __init__(self, name= '', age = 1, gender= 'M'):
        self.name = name
        self.age = age
        self.gender = gender

    def setName(self, val):
        self.name = val

    def setAge(self, val):
        try:
            age = float(val)
            if val <= 0 or val > 121:
                print('What you entered for age is out of range. Try enter between 1 to 121')
                return False
            self.age = age
        except ValueError:
            print('Invalid Input')
            return False 

    def setGender(self, val):
        if val.upper() != 'M' and val.upper() != 'F':
            print('what you entered for gender is not allowed. Only M(Male) or F(Female) are correct')
            return False
        self.gender = val

class FreshStudent(Student):
    def __init__(self, name='', age=1, gender='M', averageMark = 1, level = 'UG1'):
        super().__init__(name, age, gender)
        self.averageMark = averageMark
        self.level = level
        

    def setAverageMark(self, val):
        try:
            avg = float(val)
            if val < 1 or val > 100:
                print('what you entered for average mark is not valid. Try enter between 1 to 100')
                return False
            self.averageMark = avg
        except ValueError:
            print('Invalid Input')
            return False

       

    def setLevel(self, val):
        if val.upper() != "UG1" and val.upper() != "UG2" and val.upper() != "UG3" and val.upper() != "UG4":
            print('what you entered for level Mark is not valid. Try enter UG1, UG2, UG3 or UG4')
            return False
        self.level = val

    def displayResult(self):
        print("Student Name Age Gender Level Average Mark")
        print(f"{self.name}          {self.age}      {self.gender}    {self.level}      {self.averageMark}")


def main():
    s1 = FreshStudent()
    name = input('Please insert name of student: ')
    s1.setName(name)

    while True:
        age = int(input('Please insert age of student: '))
        if s1.setAge(age) != False:
            break

    while True:
        gender = input('Please insert gender of student: ')
        if s1.setGender(gender) != False:
            break
    
    while True:     
        averageMark = int(input('Please insert average mark of student: '))
        if s1.setAverageMark(averageMark) != False:
            break

    while True:
        level = input('Please insert level of student: ')
        if s1.setLevel(level) != False:
            break

    s1.displayResult()

main()