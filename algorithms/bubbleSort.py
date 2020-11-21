import time
from colors import *

def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
                time.sleep(timeTick)
                
    drawData(data, [BLUE for x in range(len(data))])
  