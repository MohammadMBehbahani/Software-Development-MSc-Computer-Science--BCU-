args = []
count = 0
total = 0

def calc_Avg():
    global args, count, total
    avg = 0
    while True:
        value = input('Please enter numbers to calculate average of them then press done to show the result: ')
        if value == 'done':
            break
        try:
            num = float(value)
            args.append(num)
        except ValueError:
            print('Invalid Input')
            continue
        count = count + 1
    total = sum(args)
    avg = total / count
    return total, avg

def main():
    total, avg = calc_Avg()
    print(f'your total of your numbers is {total}')
    print(f'your averag of your numbers is {avg}')
main()