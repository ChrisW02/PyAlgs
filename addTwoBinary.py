def add(A, B):
    global i
    C = [0] * (len(A) + 1)
    carry = 0
    for i in range(len(A) - 1, -1, -1):
        C[i + 1] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) // 2
    C[0] = carry
    return C


def main():
    D = add([0, 0, 1], [0, 0, 1])
    print(D)

main()