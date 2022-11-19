import time
from colors import *

def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up	
	return b	
			
def bucket_sort(data, drawData, timeTick):
	arr = []
	slot_num = 10 

	for i in range(slot_num):
		arr.append([])
		
	# Put array elements in different buckets
	for idx, j in enumerate(data):
		index_b = int(slot_num * j)
		arr[index_b].append(j)
		drawData(data,[YELLOW if x == idx else BLUE for x in range(len(data))])
	
	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])
		
	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			data[k] = arr[i][j]
			k += 1
	drawData(data,[BLUE for x in range(len(data))])
