def isleap(y):
    if y % 400 == 0:
        print("year %d is divisible by 400" %y)
        return True
    elif y % 100 == 0:
            print("year %d is divisible by 100 but not by 400" %y)
            return False
    elif y % 4 == 0:
        print("year %d is divisible by 4 but not by 100" %y)
        return True
    else:
        print("year %d is not leap year" %y)
        return False

def daysinmonth(m, y):
    if m < 1 and m > 12: 
        return
    elif isleap(y) and m == 2:
        return 29
    elif m == 2:
        return 28
    elif m == 4 or 6 or 9 or 11:
        return 30
    else:
        return 31

print(daysinmonth(2, 2010))