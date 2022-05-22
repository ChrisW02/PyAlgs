def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while key < A[j] and j >= 0:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key  # Since at last, j-=1.


def main():
    A = [3, 2, 6, 1, 6, 7, 9, 5, 4]
    insertionSort(A)
    print(A)


main()
