def counting_sort(ara):
    n = max(ara) + 1
    count = [0] * n
    for item in ara:
        count[item] +=1

    k = 0
    for i in range(n-1, -1, -1):
        for j in range(count[i]):
            ara[k] = i
            k += 1

def main():
    ara = [13, 1, 100, 99, 13, 12, 13, 99, 1, 2, 3, 3, 100, 100]
    counting_sort(ara)
    print("Sorted array: ")
    for item in ara:
        print(item, end = " ")
    print("\n")

if __name__ == "__main__":
    main()
