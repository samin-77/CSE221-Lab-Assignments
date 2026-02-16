import sys

def main():
    input_data = sys.stdin.buffer

    n = int(input_data.readline())
    A = list(map(int, input_data.readline().split()))

    m = int(input_data.readline())
    B = list(map(int, input_data.readline().split()))

    i = 0
    j = 0

    write = sys.stdout.write

    # Merge while both arrays have elements
    while i < n and j < m:
        if A[i] <= B[j]:
            write(str(A[i]) + " ")
            i += 1
        else:
            write(str(B[j]) + " ")
            j += 1

    # Output remaining elements of A (if any)
    while i < n:
        write(str(A[i]) + " ")
        i += 1

    # Output remaining elements of B (if any)
    while j < m:
        write(str(B[j]) + " ")
        j += 1

if __name__ == "__main__":
    main()
