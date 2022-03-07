import student_module as model

def main():
    m1 = model.Module("computer programming", 20, "Cyber Security")
    m2 = model.Module("Network Fundemental", 20, "Network and Distributed Systems")
    m3 = model.Module("Computer System", 20, "Digital Media")
    
    s1 = model.Student("Adam", "ID2324")
    
    s2 = model.Student("Olivia", "ID995")
    
    s1.enrol(m1)
    s1.enrol(m2)
    
    s2.enrol(m2)
    s2.enrol(m3)
    
    s1.print_student_info()
    print("\n")
    s2.print_student_info()

main()


