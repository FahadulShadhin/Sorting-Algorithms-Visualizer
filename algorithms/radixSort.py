import time
from colors import *


def countingSort(array, place, drawData, timeTick, color):
    size = len(array)
    output = [0] * size
    count = [0] * (max(array) + 1)

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, max(array) + 1):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
        drawData(output, [color for x in range(len(output))] )
        time.sleep(timeTick)

    for i in range(0, size):
        array[i] = output[i]


def radix_sort(data, drawData, timeTick):
    max_element = max(data)
    place = 1
    index = 0
    color = [YELLOW, LIGHT_GREEN, DARK_GRAY, RED, WHITE, BLACK]
    while max_element // place > 0:
        countingSort(data, place, drawData, timeTick, color[index])
        place *= 10
        index += 1
    drawData(data, [BLUE for x in range(len(data))] )