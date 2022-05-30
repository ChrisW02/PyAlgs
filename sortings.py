def selection_sort(A):
    for i in range(len(A) - 1, 0, -1):
        m = i
        for j in range(i):
            if A[j] > A[m]:
                m = j
        A[i], A[m] = A[m], A[i]


def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1


def merge_sort(A, a=0, b=None):
    if b is None: b = len(A)
    if b - a > 1:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        i, j = 0, 0
        while a < b:
            if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
                A[a] = L[i]
                i += 1
            else:
                A[a] = R[j]
                j += 1
            a += 1
