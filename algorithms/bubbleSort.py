def bubble_sort(ara):
    n = len(ara)
    for i in range(n-1):
        for j in range(n-i-1):
            if ara[j] > ara[j+1]:
                ara[j], ara[j+1] = ara[j+1], ara[j]

def main():
    ara = [10, 2, 9, 100, 11, 1, 3]
    bubble_sort(ara)

    print("Soretd array: ")
    for item in ara:
        print(item, end = " ")
    print("\n")

if __name__ == "__main__":
    main()
