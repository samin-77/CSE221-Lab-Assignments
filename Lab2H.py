import sys

def kth_not_divisible(k, x):
    lo, hi = 1, k * x  # safe upper bound

    while lo < hi:
        mid = (lo + hi) // 2

        # how many numbers ≤ mid are NOT divisible by x
        count = mid - (mid // x)

        if count >= k:
            hi = mid
        else:
            lo = mid + 1

    return lo

def main():
    input_data = sys.stdin.buffer
    t = int(input_data.readline())

    out = []
    for _ in range(t):
        k, x = map(int, input_data.readline().split())
        out.append(str(kth_not_divisible(k, x)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
