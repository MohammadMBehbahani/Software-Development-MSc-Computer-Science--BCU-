import math

A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
D = int(input("Enter D: "))
E = int(input("Enter E: "))

def mean(arr):
    sum = 0;
    for i in range(len(arr)):
        sum += arr[i]
    return sum / len(arr)

def stddev(arr):
    sigma = 0.0
    meanArr = mean(arr)
    for i in range(len(arr)):
        sigma += math.pow((arr[i] - meanArr),2)
        i += 1
    result = 0
    result = math.sqrt(sigma/(len(arr)))
    return result


arr = [A, B, C, D, E]
print(stddev(arr))