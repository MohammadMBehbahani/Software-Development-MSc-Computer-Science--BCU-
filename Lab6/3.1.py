import person_module

class Lecturer(person_module.StaffMember):
    def __init__(self, name, phone_number, academic_title, salary):
        super().__init__(salary, name, phone_number)
        self._academic_title = academic_title
    
    def __str__(self):
        return super().get_profile_info() + ", salary: {}, academic_title: {}".format(super().get_salary(), self._academic_title)
        
def main():
    Lec1 = Lecturer("mohammad", "pn1", "Sofware1", 19000)
    Lec2 = Lecturer("mohammad2", "pn2", "Sofware2", 20000)
    Lec3 = Lecturer("mohammad3", "pn3", "Sofware3", 21000)

    print(Lec1)
    print(Lec2)
    print(Lec3)

main()