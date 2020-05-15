def insertion_sort(ara):
    n = len(ara)

    for i in range(n):
        temp = ara[i]
        k = i
        while k > 0 and temp < ara[k-1]:
            ara[k] = ara[k-1]
            k -= 1
            ara[k] = temp

def main():
    ara = [10, 2, 9, 100, 11, 1, 3]
    insertion_sort(ara)

    print("Sorted array: ")
    for item in ara:
        print(item, end = " ")
    print("\n")

if __name__ == "__main__":
    main()
