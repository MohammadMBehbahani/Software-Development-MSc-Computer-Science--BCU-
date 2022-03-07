def question():
    print("What is capital of US? ")
    list_answ = ["NewYourk", "LosAngles", "Washington", "None above"]
    
    i = 1
    for answ in list_answ:
        print("{} {}".format(i, answ))
        i += 1            

chance_of_wrong_answ = 3


def ask_question():
    question()
    answ = int(input("Please enter your answer: "))
    
    global chance_of_wrong_answ
    
    while chance_of_wrong_answ > 0:
        if answ == 4:
            print("Your answer is correct")
            break
        else:
            chance_of_wrong_answ -= 1
            print("Wrong answer")
            print("you have {} more chance".format(chance_of_wrong_answ))
            main()

def while_test_decending():
    i = 10
    while i > 0 :
        print(i)
        i -= 1



def sent():
    myList = ["Earth", "revolves", "around", "the", "and", "has", "an",
              "atmosphere", "containing", "21", "percent", "of "]
    
    my_answ = ['sun - oxyzen', 'oxyzen - sun', 'water - dust', 'none above']
    
    string_final = ''
    for idx, value in enumerate(myList):
        if idx == 3:
            string_final += value + ' ... '
        elif idx == 11:
            string_final += '... '
        else:
            string_final += value + " "
    print(string_final)
    print("Please fill in the blank with follinw answer")
    
    for answ in my_answ:
        print(answ)
    

def check_type():
    value = input("Number: ")
    
    try:
       val = int(value)
       print("Number = ", val ** 2)
       
    except ValueError:
       try:
           val = float(value)
           print("Number = ", val ** 2)
       except ValueError:
           print("Sorry Man, I'm afraid I can't do that")


def main():
   check_type()
   
main()