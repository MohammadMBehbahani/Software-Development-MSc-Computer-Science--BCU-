def calculation(num_1, num_2, opr):
    if opr == "+":
        res = num_1 + num_2
        return f"Adding {num_1} by {num_2} = {res}"
    elif opr == "*":
        res = num_1 * num_2
        return f"Multiplying {num_1} by {num_2} = {res}"
    elif opr == "-":
        res = num_1 - num_2
        return f"Submission {num_1} by {num_2} = {res}"
    elif opr == "/":
        res = num_1 / num_2
        return f"Division {num_1} by {num_2} = {res}"
    else: 
        print("Wrong number!! Please Enter valid number")


def select_opr():
    opr = input("Please select your operator ['+', '-', '*', '/']: ")
    return opr 

def take_val(i):
    num = int(input(f"Please Enter Number{i} : "))
    return num
