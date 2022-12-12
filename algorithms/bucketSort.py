import time
from colors import *

			
def bucket_sort(data, drawData, timeTick, insertion_sort):
	arr = []
	slot_num = 10

	for i in range(slot_num):
		arr.append([])
		
	# Put array elements in different buckets
	for j in data:
		index_b = int(slot_num * j)
		arr[index_b].append(j)
	
	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertion_sort(arr[i], drawData, timeTick)
		
	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			data[k] = arr[i][j]
			k += 1
	drawData(data,[BLUE for x in range(len(data))])
