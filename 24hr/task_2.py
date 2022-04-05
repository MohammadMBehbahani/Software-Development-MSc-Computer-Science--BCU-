class Service:
    def __init__(self, name):
        self._name = name

    def service_Fare(self):
        if self._name == 'bus':
                    return 26.00
        elif self._name == 'taxi':
                    return 45.00
        elif self._name == 'train':
                    return 57
        elif self._name == 'aeroplane':
                    return 135.00

    def calc_Fare(self, countBag, weight):
        if countBag <= 2 and weight <= 50:
            if self._name == 'bus':
                    fare= (self.service_Fare() * 5) / 100
                    totalfare = self.service_Fare() + fare
                    display_msg(totalfare, fare)

            elif self._name ==  'taxi':
                    fare= (self.service_Fare() * 10) / 100
                    totalfare = self.service_Fare() + fare
                    display_msg(totalfare, fare)

            elif self._name == 'train':
                    fare= (self.service_Fare() * 15) / 100
                    totalfare = self.service_Fare() + fare
                    display_msg(totalfare, fare)

            elif self._name == 'aeroplane':
                    fare= (self.service_Fare() * 20) / 100
                    totalfare = self.service_Fare() + fare
                    display_msg(totalfare, fare)

        else:
            print(f"Your total fare is £{self.service_Fare()}")
            print('You have not been charged additional fee')

def display_msg(totalfare, fare):
    print(f"Your total fare is £{totalfare}")
    print(f'You have been charged £{fare} additional fee')

def select_Service():
    print('1- bus')
    print('2- taxi')
    print('3- train')
    print('4- aeroplane')

    value = int(input('Please Select Your Service: \n'))

    if value == 1:
            return 'bus'
    elif value == 2:
            return 'taxi'
    elif value == 3:
            return 'train'
    elif value == 4:
            return 'aeroplane'

def enter_countbag_totalweight():
    countbag = int(input('Please enter number of Your bags: \n'))
    totalweight = int(input('Please enter Your total weight: \n'))
    return countbag, totalweight

def main():
   countbag, totalweight = enter_countbag_totalweight()
   service = select_Service()
   
   s1 = Service(service)
   print(f"You have {countbag} bags with total weight of {totalweight}kg ")
   s1.calc_Fare(countbag, totalweight)

main()