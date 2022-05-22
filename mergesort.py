def mergesort(A):
    if len(A) > 1:
        r = len(A) // 2
        L = A[:r]
        R = A[r:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


def main():
    A = [3, 2, 6, 1, 6, 7, 9, 5, 4]
    mergesort(A)
    print(A)


main()

# import sys
#
#
# def merge(A, p, q, r):
#     n1 = q - p + 1
#     n2 = r - q
#
#     L = [0] * (n1 + 1)
#     R = [0] * (n2 + 1)
#
#     for i in range(n1):
#         L[i] = A[p + i]
#     for j in range(n2):
#         R[j] = A[q + j - 1]
#
#     L[n1] = sys.maxsize
#     R[n2] = sys.maxsize
#     i, j = 0, 0
#
#     for k in range(p, r + 1):
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         elif A[k] == R[j]:
#             j += 1
#
#
# def mergesort(A, p, r):
#     if p < r:
#         q = (p + r) // 2
#         mergesort(A, p, q)
#         mergesort(A, q + 1, r)
#         merge(A, p, q, r)
#
