import math

class Bmi:
    def __init__(self, weight: float, height: float, bmi: float):
        self.__weight = weight
        self.__height = height
        self.__bmi = bmi
    
    @property
    def weight(self):
         return self.__weight
    
    @weight.setter
    def set_weight(self, val):
        self.__weight = val
    
    @property
    def height(self):
         return self.__height
    
    @height.setter
    def set_height(self, val):
        self.__height = val
    
    @property
    def bmi(self):
         return self.__bmi
    
    @bmi.setter
    def set_bmi(self, val):
        self.__bmi = val
    
    def __str__(self):
         return str(self.__weight / math.pow((self.__height / 100), 2))
     

def main():
    myBmi = Bmi(2, 4, 6)
    print(myBmi)
    
main()