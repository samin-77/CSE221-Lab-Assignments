import sys

def main():
    data = sys.stdin.buffer.readline().split()
    n = int(data[0])
    K = int(data[1])

    arr = list(map(int, sys.stdin.buffer.readline().split()))

    freq = {}
    left = 0
    best = 0

    for right in range(n):
        val = arr[right]
        freq[val] = freq.get(val, 0) + 1

        # Shrink window if too many distinct elements
        while len(freq) > K:
            left_val = arr[left]
            freq[left_val] -= 1
            if freq[left_val] == 0:
                del freq[left_val]
            left += 1

        # Update best length
        best = max(best, right - left + 1)

    print(best)

if __name__ == "__main__":
    main()
