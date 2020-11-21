import time
from colors import *

def selection_sort(data, drawData, timeTick):
    for i in range(len(data)-1):
        minimum = i
        for k in range(i+1, len(data)):
            if data[k] < data[minimum]:
                minimum = k

        data[minimum], data[i] = data[i], data[minimum]
        drawData(data, [YELLOW if x == minimum or x == i else BLUE for x in range(len(data))] )
        time.sleep(timeTick)
        
    drawData(data, [BLUE for x in range(len(data))])
    