class calculatconsumption:
    def __init__(self, dName, pcW, nH):
        self.dname = dName
        self.pcw = pcW
        self.nh = nH
        

    def energy_consumption(self):
        return ((self.pcw * self.nh) / 1000)


class displayEnergyconsumption(calculatconsumption):
    def __init__(self, dName, pcW, nH, electricity_rate):
        self.electricity_rate = electricity_rate
        super().__init__(dName, pcW, nH)

    def calculate_energy_consumption_per_month(self):
        return (self.electricity_rate * super().energy_consumption()) * 30
    
    def printresult(self):
        print("Device_Name Power_Consumption Daily_Usage Monthly_Running_Cost")
        print("{} {:.2f} {:.2f} {}".format(self.dname, self.pcw, self.nh, self.calculate_energy_consumption_per_month()))

def get_info():
    dName = input('enter device name: ')
    pcW =input('enter power consumption in watts: ')
    nH =input('enter daily usage in hours: ')
    return dName, pcW, nH


def main():
    dName, pcW, nH = get_info()
    d1 = displayEnergyconsumption(dName, float(pcW), float(nH), 0.10)
    d1.printresult()

main()