def merge(ara, start, mid, end):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(ara[q])
            q+=1
        elif q > end:
            tempArray.append(ara[p])
            p+=1
        elif ara[p] < ara[q]:
            tempArray.append(ara[p])
            p+=1
        else:
            tempArray.append(ara[q])
            q+=1

    for p in range(len(tempArray)):
        ara[start] = tempArray[p]
        start+=1

def merge_sort(ara, start, end):
    if start < end:
        mid = int((start+end)/2)
        merge_sort(ara, start, mid)
        merge_sort(ara, mid+1, end)

        merge(ara, start, mid, end)

def main():
    ara = [10, 2, 9, 100, 11, 1, 3]
    n = len(ara)
    merge_sort(ara, 0, n-1)

    print("sorted array: ")
    for item in ara:
        print(item, end = " ")
    print("\n")

if __name__ == "__main__":
    main()
