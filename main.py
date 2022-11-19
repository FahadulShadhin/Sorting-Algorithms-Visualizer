from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import random
from colors import *

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.bucketSort import bucket_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort



# Main window 
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)


algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Bucket Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort', 'Radix Sort']
speed_list = ['Fast', 'Medium', 'Slow']


# Drawing the numerical array as bars
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


# Read data from the txt file
def read_data():
    global data

    data = []
    with open(paths) as f:
        content = f.read()
        data = content.split(' ')
    data = [float(x) for x in data]
    drawData(data, [BLUE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.8
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Bucket Sort':
        bucket_sort(data, drawData, timeTick, insertion_sort)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    else:
        counting_sort(data, drawData, timeTick)

def select_multiple():
    global paths
    paths = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=(("txt files","*.txt"),))
    entry1.configure(state=NORMAL)
    entry1.delete(0,END)
    entry1.insert(0,paths)
    entry1.configure(state='disabled')
    
    # input data file
    read_data()



# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):

    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


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

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=2, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=4, column=0, padx=10, pady=5)

b1 = Button(UI_frame,text="Sort",bg="gray26",width=6,height=1,fg="white",font=("arial 8 bold"),command=sort)
b1.grid(row=3, column=1, padx=5, pady=5)
changeOnHover(b1,"seaGreen1","gray26")


window.mainloop()