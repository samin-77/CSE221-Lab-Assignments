import sys

def main():
    data = sys.stdin.buffer.readline().split()
    n = int(data[0])
    m = int(data[1])
    K = int(data[2])

    A = list(map(int, sys.stdin.buffer.readline().split()))
    B = list(map(int, sys.stdin.buffer.readline().split()))

    i = 0
    j = m - 1

    best_diff = 10**30
    best_i = 0
    best_j = 0

    while i < n and j >= 0:
        s = A[i] + B[j]
        diff = abs(s - K)

        if diff < best_diff:
            best_diff = diff
            best_i = i
            best_j = j

        # Move pointers to get closer to K
        if s > K:
            j -= 1
        elif s < K:
            i += 1
        else:
            # Perfect match
            break

    # Output 1-based indices
    print(best_i + 1, best_j + 1)

if __name__ == "__main__":
    main()
