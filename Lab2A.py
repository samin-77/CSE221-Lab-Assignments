import sys

def main():
    data = sys.stdin.buffer.readline().split()
    n = int(data[0])
    S = int(data[1])

    arr = list(map(int, sys.stdin.buffer.readline().split()))

    left = 0
    right = n - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == S:
            # 1-based indices required
            print(left + 1, right + 1)
            return
        elif s < S:
            left += 1
        else:
            right -= 1

    print(-1)

if __name__ == "__main__":
    main()
