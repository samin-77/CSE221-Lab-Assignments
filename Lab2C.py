import sys

def main():
    data = sys.stdin.buffer.readline().split()
    n = int(data[0])
    x = int(data[1])
    arr = list(map(int, sys.stdin.buffer.readline().split()))
    
    # Store value with original index (1-based)
    a = [(arr[i], i + 1) for i in range(n)]
    a.sort()  # sort by value

    for i in range(n):
        target = x - a[i][0]

        left = i + 1
        right = n - 1

        while left < right:
            s = a[left][0] + a[right][0]

            if s == target:
                print(a[i][1], a[left][1], a[right][1])
                return
            elif s < target:
                left += 1
            else:
                right -= 1

    print(-1)

if __name__ == "__main__":
    main()
