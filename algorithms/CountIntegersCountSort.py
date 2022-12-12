import time
from colors import *

def findNoOfIntegersInRange(data, a, b, drawData, timeTick):
    size = len(data)

    count = [0] * (max(data)+1)

    for i in range(0, size):
        count[data[i]] += 1

    for i in range(1, max(data)+1):
        count[i] += count[i - 1]

    numbers = []

    for i in range(a-1, b):
        if i+1 < len(count) and (count[i] - count[i+1]) != 0:
            numbers.append(i+1)

    drawData(data, [YELLOW if x in numbers else BLUE for x in data])

    return len(numbers)