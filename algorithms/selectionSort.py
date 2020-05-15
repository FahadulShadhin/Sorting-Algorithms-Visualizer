def selection_sort(ara):
    n = len(ara)

    for i in range(n-1):
        minimum = i
        for k in range(i+1, n):
            if ara[k] < ara[minimum]:
                minimum = k

        ara[minimum], ara[i] = ara[i], ara[minimum]

def main():
    ara = [10, 2, 9, 100, 11, 1, 3]
    selection_sort(ara)

    print("Sorted array: ")
    for item in ara:
        print(item, end = " ")
    print("\n")

if __name__ == "__main__":
    main()
