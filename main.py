from tkinter import *
from tkinter import ttk
import random
from colors import *

### IMPORTING SORTING ALGORITHMS ###
from bubbleSort import bubble_sort_ascending, bubble_sort_descending
from selectionSort import selection_sort_ascending, selection_sort_descending
from insertionSort import insertion_sort_ascending, insertion_sort_descending
from mergeSort import merge_sort_ascending, merge_sort_descending
from quickSort import quick_sort_ascending, quick_sort_descending
from heapSort import heap_sort_ascending, heap_sort_descending
from countingSort import counting_sort_ascending, counting_sort_descending
#####################################


### MAIN WINDOW ###
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)
###################


# SOME VARIABLES :/
algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']


### DRAWING THE GRIDS ###
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


### GENERATE RANDOM UNSORTED ARRAY ###
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


# Setting sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


### SORTING IN ASCENDING ORDER ###
def sort_ascending():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort_ascending(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort_ascending(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort_ascending(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort_ascending(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort_ascending(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort_ascending(data, drawData, timeTick)
    else:
        counting_sort_ascending(data, drawData, timeTick)


### SORTING IN DESCENDING ORDER ###
def sort_descending():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort_descending(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort_descending(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort_descending(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort_descending(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort_descending(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort_descending(data, drawData, timeTick)
    else:
        counting_sort_descending(data, drawData, timeTick)



### USER INTERFACE ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# '#FCF3CF'
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort in Ascending Oreder", command=sort_ascending, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b2 = Button(UI_frame, text="Sort in Descending Oreder", command=sort_descending, bg=LIGHT_GRAY)
b2.grid(row=2, column=2, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)
###


window.mainloop()
