import time
from colors import *

def counting_sort(data, drawData, timeTick):
    size = len(data)
    output = [0] * size

    count = [0] * (max(data)+1)

    for i in range(0, size):
        count[data[i]] += 1

    for i in range(1, max(data)+1):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[data[i]] - 1] = data[i]
        count[data[i]] -= 1
        i -= 1
        drawData(output, [BLUE for x in range(len(output))] )
        time.sleep(timeTick)

    for i in range(0, size):
        data[i] = output[i]
    # drawData(data, [BLUE for x in range(len(data))])