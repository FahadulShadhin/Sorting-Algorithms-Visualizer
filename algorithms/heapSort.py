def heapify(ara, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and ara[i] < ara[left]:
        largest = left

    if right < n and ara[largest] < ara[right]:
        largest = right

    if largest != i:
        ara[i], ara[largest] = ara[largest], ara[i]
        heapify(ara, n, largest)

def heap_sort(ara):
    n = len(ara)

    for i in range(n-1, -1, -1):
        heapify(ara, n, i)

    for i in range(n-1, 0, -1):
        ara[i], ara[0] = ara[0], ara[i]
        heapify(ara, i, 0)

def main():
    ara = [10, 2, 9, 100, 11, 1, 3]
    heap_sort(ara)

    print("Sorted array is: ")
    for item in ara:
        print(item, end = " ")
    print("\n")

if __name__ == "__main__":
    main()
