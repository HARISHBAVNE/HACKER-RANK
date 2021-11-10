def sort(l):
    numberOfSwaps = 0
    n = len(l)
    for i in range(n):
        for j in range(n-1):
            if (l[j] > l[j+1]):
                numberOfSwaps += 1
                l[j],l[j+1] = l[j+1],l[j]
    print(f"Array is sorted in {numberOfSwaps} swaps.")
    print(f"First Element: {l[0]}")
    print(f"Last Element: {l[n-1]}")
def main():
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    sort(a)

if __name__ == "__main__":
    main()