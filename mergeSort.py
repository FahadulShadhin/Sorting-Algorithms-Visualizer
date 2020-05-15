import time
from colors import *

def merge_ascending(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def merge_sort_ascending(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort_ascending(data, start, mid, drawData, timeTick)
        merge_sort_ascending(data, mid+1, end, drawData, timeTick)

        merge_ascending(data, start, mid, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

#
#
#

def merge_descending(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] > data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def merge_sort_descending(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort_descending(data, start, mid, drawData, timeTick)
        merge_sort_descending(data, mid+1, end, drawData, timeTick)

        merge_descending(data, start, mid, end, drawData, timeTick)

        drawData(data, [DARK_BLUE if x >= start and x < mid else YELLOW if x == mid 
                        else PURPLE if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
