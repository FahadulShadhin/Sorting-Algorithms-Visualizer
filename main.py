from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from colors import *
from buttonProperties import changeOnHover
import time

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.bucketSort import bucket_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort
from algorithms.radixSort import radix_sort
from algorithms.hybridSort import hybrid_quick_sort

''' --------------------------------------------------------------------------------------------------'''

# Main window 
window = Tk()
window.title("Sorting Visualizer")
window.maxsize(1300, 700)
window.config(bg = WHITE)


algorithm_name = StringVar()
speed_name = StringVar()
# data = []
# originalData = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Bucket Sort', 'Merge Sort', 'Quick Sort',
                 'Heap Sort', 'Counting Sort', 'Radix Sort','Hybrid Sort']
speed_list = ['Fast', 'Medium', 'Slow']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 1300
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


# Read data from the txt file
def read_data():
    global data, originalData
    data = []
    l4.config(text="")
    l5.config(text="")

    # reading from the input file
    with open(paths) as f:
        content = f.read()

        # Spliting the numbers on the basis of space delimiter
        data = content.split(' ')

    # flag variable by default tells that data list contains only positive numbers    
    flag = False

    if type(data[0]) == str:
        data = [float(x) if x != '' or x != ' ' else 10 for x in data]

    # Checking whether the data contains negative or not
    for x in data:
        if x < 0:
            flag = True
            break

    # If len of data is less than 2 and it contians negative numbers that clear tha data list
    if len(data) < 2 or flag :
        data = []

    print(len(data))

    # Copy the data list to save it for the reset feature
    originalData = data.copy()

    # Draw the data list on the Canvas
    drawData(data, [BLUE for x in range(len(data))])


# Resetting the canvas with input numbers sequence
def reset():
    data = []
    l4.config(text="")
    l5.config(text="")
    data = originalData.copy()
    drawData(data, [BLUE for x in range(len(data))])


# Setting the Visualization speed of the Sorting Algorithms
def set_speed():
    if speed_menu.get() == 'Slow':
        return 3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.0001


# Calls selected sorting algorithm in the combobox
def sort():
    timeTick = set_speed()
    start = end = 0
    spaceComplexity = ""
    
    if algo_menu.get() == 'Bubble Sort':
        start = time.time()
        bubble_sort(data, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(1)"
    elif algo_menu.get() == 'Bucket Sort':
        start = time.time()
        bucket_sort(data, drawData, timeTick, insertion_sort)
        end = time.time()
        spaceComplexity = "O(n)"
    elif algo_menu.get() == 'Insertion Sort':
        start = time.time()
        insertion_sort(data, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(1)"
    elif algo_menu.get() == 'Merge Sort':
        start = time.time()
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(n)"
    elif algo_menu.get() == 'Quick Sort':
        start = time.time()
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(1)"
    elif algo_menu.get() == 'Heap Sort':
        start = time.time()
        heap_sort(data, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(1)"
    elif algo_menu.get() == 'Counting Sort':
        start = time.time()
        counting_sort([int(x) for x in data], drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(k)"
    elif algo_menu.get() == 'Radix Sort':
        start = time.time()
        radix_sort([int(x) for x in data], drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(n+k)"
    elif algo_menu.get() == 'Hybrid Sort':
        start = time.time()
        hybrid_quick_sort(data, 0, len(data)-1, drawData, timeTick)
        end = time.time()
        spaceComplexity = "O(1)"
    else:
        y = 0

    l4.config(text = "Time : "+ str(round( (end-start), 3) ) + " sec")
    l5.config(text="Space Complexity : "+spaceComplexity)

# Browse the input file
def select_multiple():
    global paths

    # Only one input file is allowable at a time
    paths = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=(("txt files","*.txt"),))
    entry1.configure(state=NORMAL)
    entry1.delete(0,END)
    entry1.insert(0,paths)
    entry1.configure(state='disabled')
    
    # input data file
    read_data()


''' --------------------------------------------------------------------------------------------------'''


### User interface ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)


l3 = Label(UI_frame, text="Choose File: ", bg=WHITE)
l3.grid(row=0, column=0, padx=10, pady=5, sticky=W)

# Select the input data file
text1 = StringVar()
entry1 = Entry(UI_frame,textvariable=text1, bd=2,width=23)
entry1.grid(row=0,column=1,padx=10, pady=5, sticky=W)
entry1.insert(0,os.getcwd())
entry1.configure(state='disabled')

b2 = Button(UI_frame,text="Browse",bg="gray26",width=6,height=1,fg="white",font=("arial 8 bold"),command=select_multiple)
b2.grid(row=0, column=2, padx=5, pady=5)
changeOnHover(b2,"seaGreen1","gray26")


l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=1, column=1, padx=5, pady=5)
algo_menu.current(0)
b3 = Button(UI_frame,text="Reset",bg="gray26",width=6,height=1,fg="white",font=("arial 8 bold"),command=reset)
b3.grid(row=1, column=2, padx=5, pady=5)
changeOnHover(b3,"seaGreen1","gray26")

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=2, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=1300, height=400, bg=WHITE)
canvas.grid(row=4, column=0, padx=10, pady=5)

b1 = Button(UI_frame,text="Sort",bg="gray26",width=6,height=1,fg="white",font=("arial 8 bold"),command=sort)
b1.grid(row=3, column=1, padx=5, pady=5)
changeOnHover(b1,"seaGreen1","gray26")


l4 = Label(UI_frame, text="", bg=WHITE)
l4.grid(row=5, column=0, padx=10, pady=5, sticky=W)

l5 = Label(UI_frame, text="", bg=WHITE)
l5.grid(row=5, column=1, padx=10, pady=5, sticky=W)

window.mainloop()