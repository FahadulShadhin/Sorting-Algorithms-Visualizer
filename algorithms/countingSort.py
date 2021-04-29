# Counting sort is not a comperison-based algorithm like the others.
# This algorithm counts the frequency of every unique element in a range.
# If the maximum value of the array is large it is not a good idea to use counting sort.
# But as in this case data[] is generating values between 1 to 150, counting sort works just fine :)

import time
from colors import *

def counting_sort(data, drawData, timeTick):
    n = max(data) + 1
    count = [0] * n
    for item in data:
        count[item] += 1
    
    k = 0
    for i in range(n):
        for j in range(count[i]):
            data[k] = i
            drawData(data, [BLUE for x in range(len(data))] )
            time.sleep(timeTick)
            k += 1

    drawData(data, [BLUE for x in range(len(data))])

