class calculatconsumption:
    def __init__(self, dName, pcW, nH):
        self.dname = dName
        self.pcw = pcW
        self.nh = nH
        
    def energy_consumption_per_day(self):
        return ((self.pcw * self.nh) / 1000)


class displayEnergyconsumption(calculatconsumption):
    def __init__(self, dName = '', pcW = '', nH = '', electricity_rate= 0.10):
        self.electricity_rate = electricity_rate
        super().__init__(dName, pcW, nH)

    def calculate_energy_consumption_per_month(self):
        return (self.electricity_rate * super().energy_consumption_per_day()) * 30
    
    def calculate_energy_consumption_per_annual(self):
        return (self.electricity_rate * super().energy_consumption_per_day()) * 365

    def manitor_device(self, budget):
        devicelist = []
        sum_annualCost = 0
        sum_monthCost = 0
        for i in range(3):
            dName, pcW, nH = get_info()
            self.dname = dName
            self.pcw = int(pcW)
            self.nh = int(nH)
            context = {
                'dName': self.dname,
                'pcw': self.pcw,
                'nh': self.nh,
                'calculate_energy_consumption_per_month': self.calculate_energy_consumption_per_month(),
                'calculate_energy_consumption_per_annual': self.calculate_energy_consumption_per_annual()
            }

            devicelist.append(context)
            sum_monthCost += sum_monthCost + self.calculate_energy_consumption_per_month()
            sum_annualCost += sum_annualCost + self.calculate_energy_consumption_per_annual()
        
        print("Device_Name Power_Consumption Daily_Usage Monthly_Running_Cost Annual_Running_Cost")
        for item in devicelist:
            print("{} {:.2f} {:.2f} {} {}".format(item['dName'], item['pcw'], item['nh'], item['calculate_energy_consumption_per_month'], item['calculate_energy_consumption_per_annual']))
        
        print("your month running cost for these three device is: ", sum_monthCost)
        print("your annual running cost for these three device is:", sum_annualCost)

        if sum_annualCost > budget:
            print('your annual running cost for these three devices is above your budget')
        elif sum_annualCost == budget:
            print('your annual running cost for these three devices is equal your budget')
        else:
            print('your annual running cost for these three devices is lower your budget')




    def printresult(self):
        print("Device_Name Power_Consumption Daily_Usage Monthly_Running_Cost")
        print("{} {:.2f} {:.2f} {}".format(self.dname, self.pcw, self.nh, self.calculate_energy_consumption_per_month()))

def get_info():
    dName = input('enter device name: ')
    pcW =input('enter power consumption in watts: ')
    nH =input('enter daily usage in hours: ')
    return dName, pcW, nH



    

def main():
   ex1= displayEnergyconsumption()
   annual_budget = float(input('Please enter your annual budget: '))
   ex1.manitor_device(annual_budget)
main()