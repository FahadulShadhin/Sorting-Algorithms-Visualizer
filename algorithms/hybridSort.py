import time
from colors import *


def insertion_sort(arr, low, n, drawData, timeTick):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j>low and arr[j-1]>val:
            arr[j]= arr[j-1]
            j-= 1
        arr[j]= val
        drawData(arr, [YELLOW if x == i else RED if x == j else LIGHT_GREEN for x in range(len(arr))])
        time.sleep(timeTick)  
    drawData(arr, [BLUE for x in range(len(arr))])

 
def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i]<pivot:
            arr[i], arr[j]= arr[j], arr[i]
            j+= 1
    arr[j], arr[high]= arr[high], arr[j]
    return j
 
 
def hybrid_quick_sort(arr, low, high, drawData, timeTick):
    while low<high:
 
        if high-low + 1<10:
            insertion_sort(arr, low, high, drawData, timeTick)
            break
 
        else:
            pivot = partition(arr, low, high)
 
            if pivot-low<high-pivot:
                hybrid_quick_sort(arr, low, pivot-1, drawData, timeTick)
                low = pivot + 1
            else:
                hybrid_quick_sort(arr, pivot + 1, high, drawData, timeTick)
                high = pivot-1
            
            drawData(arr, [PURPLE if x >= low and x < pivot else YELLOW if x == pivot else PINK if x > pivot and x <=high else BLUE for x in range(len(arr))])
            time.sleep(timeTick)

            
    drawData(arr, [BLUE for x in range(len(arr))])