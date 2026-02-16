import sys

def main():
    data = sys.stdin.buffer.readline().split()
    n = int(data[0])
    K = int(data[1])

    arr = list(map(int, sys.stdin.buffer.readline().split()))

    left = 0
    current_sum = 0
    best = 0

    for right in range(n):
        current_sum += arr[right]

        # Shrink window until valid
        while current_sum > K and left <= right:
            current_sum -= arr[left]
            left += 1

        # Update longest valid length
        best = max(best, right - left + 1)

    print(best)

if __name__ == "__main__":
    main()
