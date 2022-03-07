import Calculation

def display_msg(msg):
    print(msg)

def main():
   num_1 = Calculation.take_val(1)
   num_2 = Calculation.take_val(2)
   opr = Calculation.select_opr()
   
   print(Calculation.calculation(num_1, num_2, opr))

main()