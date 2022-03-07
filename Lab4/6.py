import math

current_x = 0
current_y = 0

def calc_distance(x2, y2):
    global current_x
    global current_y
    
    res = math.sqrt(pow((x2 - current_x), 2) + pow((y2 - current_y), 2))
    
    current_x = x2
    current_y = y2
    
    return res

def robot_move():
    distances = []
    
    while True:
        x2 = int(input("please insert destination X2 value: "))
        y2 = int(input("please insert destination Y2 value: "))
        if x2 == 999 and y2 == 999:
            i = 1
            sum_distance = 0
            for distance in distances:
                sum_distance = sum_distance + distance
                print("Step {}: {:.2f}".format(i, distance))
                i += 1
            print("total distance (in meters) the robot has moved is : {:.2f}".format(sum_distance))
            break
        else:
          distances.append(calc_distance(x2, y2))

def main():
    robot_move()

main()