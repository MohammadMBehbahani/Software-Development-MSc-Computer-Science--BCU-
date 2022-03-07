class Employee:
    def __init__(self, name, address, age, worked_h_pw, pay_rate):
        self._name = name
        self._address = address
        self._age = age
        self._wkpw = worked_h_pw
        self._pr = pay_rate
    
    def wsbtx(self):
        salary = self._wkpw * self._pr 
        return salary
    
    def wsatx(self):
        salary = self._wkpw * self._pr 
        
        if self._age < 50:
            salary = salary - ((salary * 20) / 100)
        else:
            salary = salary - ((salary * 5) / 100)
            
        return salary
    
    def printdetail(self):
        print("Employee {} with {} years old and his/her address is {} with work salary before tax {} with work salary after tax {}"
              .format(self._name, self._age, self._address, self.wsbtx(), self.wsatx()))
        

def main():
    emp1= Employee("Mohammad", "address 1", 20, 20, 7)
    
    emp1.printdetail()

main()