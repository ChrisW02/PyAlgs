def max_heapify(A,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    lgs = i
    if l < n:
        if A[l] > A[i]:
            lgs = l
    if r < n:
        if A[r] > A[i]:
            lgs = r
    if lgs != i:
        swap(A, lgs, i)
        max_heapify(A, n,lgs)


def build_max_heap(A):
    n = len(A)
    for k in range(n // 2 - 1, -1, -1):
        max_heapify(A,n,k)


def heap_sort(A):
    n = len(A)
    build_max_heap(A)
    for i in range(n - 1, 0, -1):
        swap(A, 0, i)
        max_heapify(A,i, 0)


def swap(A, a, b):
    temp = A[a]
    A[a] = A[b]
    A[b] = temp


def main():
    A = [3, 2, 6, 1, 6, 7, 9, 5, 4]
    heap_sort(A)
    print(A)


main()
