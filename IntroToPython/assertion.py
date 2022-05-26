def avg(A):
    assert len(A) != 0, "No data!"
    return sum(A) / len(A)

def main():
    print(avg([]))

main()