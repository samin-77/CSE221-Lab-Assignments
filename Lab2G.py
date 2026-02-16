import sys

def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo

def main():
    input_data = sys.stdin.buffer

    n, q = map(int, input_data.readline().split())
    arr = list(map(int, input_data.readline().split()))

    out_lines = []

    for _ in range(q):
        x, y = map(int, input_data.readline().split())

        left = lower_bound(arr, x)
        right = upper_bound(arr, y)

        out_lines.append(str(right - left))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
