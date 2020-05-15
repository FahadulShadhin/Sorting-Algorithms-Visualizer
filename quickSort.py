import time
from colors import *

def partition_ascending(data, start, end, drawData, timeTick):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quick_sort_ascending(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition_ascending(data, start, end, drawData, timeTick)
        quick_sort_ascending(data, start, pivot_position-1, drawData, timeTick)
        quick_sort_ascending(data, pivot_position+1, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                        else DARK_BLUE if x > pivot_position and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, [BLUE for x in range(len(data))])

#
#
#

def partition_descending(data, start, end, drawData, timeTick):
    i = start + 1
    pivot = data[start]

    for j in range(start+1, end+1):
        if data[j] > pivot:
            data[i], data[j] = data[j], data[i]
            i+=1
    data[start], data[i-1] = data[i-1], data[start]
    return i-1

def quick_sort_descending(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition_descending(data, start, end, drawData, timeTick)
        quick_sort_descending(data, start, pivot_position-1, drawData, timeTick)
        quick_sort_descending(data, pivot_position+1, end, drawData, timeTick)

        drawData(data, [DARK_BLUE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                        else PURPLE if x > pivot_position and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, [BLUE for x in range(len(data))])
