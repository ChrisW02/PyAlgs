'''
Sorting in Lec 3.
All using recursive ways to implement.
'''

'''
Selection Sort: O(n^2)
'''

def selectionSort(A, i=None):
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selectionSort(A, i - 1)


def prefix_max(A, i):
    if i > 0:
        j = prefix_max(A, i - 1)
        if A[j] > A[i]:
            return j
    return i

'''
Insert Sort: O(n^2)
'''

def insertSort(A, i=None):
    if i is None: i = len(A) - 1
    if i > 0:
        insertSort(A, i - 1)
        insert_last(A, i)


def insert_last(A, i):
    if i > 0 and A[i] < A[i - 1]:
        A[i], A[i - 1] = A[i - 1], A[i]
        insert_last(A, i - 1)

'''
Merge Sort: O(nlogn)
'''

def mergeSort(A, a=0, b=None):
    if b is None: b = len(A)
    if b - a > 1:
        c = (a + b + 1) // 2
        mergeSort(A, a, c)
        mergeSort(A, c, b)
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)


def merge(L, R, A, i, j, a, b):
    if a < b:
        if (j <= 0) or (L[i - 1] > R[j - 1] and i > 0):
            A[b - 1] = L[i - 1]
            i -= 1
        if (i <= 0) or (R[j - 1] > L[i - 1] and j > 0):
            A[b - 1] = R[j - 1]
            j -= 1
        merge(L, R, A, i, j, a, b - 1)
