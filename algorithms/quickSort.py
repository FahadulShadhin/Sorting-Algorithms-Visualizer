def partition(ara, start, end):
    i = start + 1
    pivot = ara[start]

    for j in range(start+1, end+1):
        if ara[j] < pivot:
            ara[i], ara[j] = ara[j], ara[i]
            i += 1
    ara[start], ara[i-1] = ara[i-1], ara[start]
    return i-1

def quick_sort(ara, start, end):
    if start < end:
        pivot_position = partition(ara, start, end)
        quick_sort(ara, start, pivot_position-1)
        quick_sort(ara, pivot_position+1, end)

def main():
    ara = [10, 2, 9, 100, 11, 1, 3]
    n = len(ara)
    quick_sort(ara, 0, n-1)

    print("Sorted array: ")
    for item in ara:
        print(item, end = " ")
    print("\n")

if __name__ == "__main__":
    main()
