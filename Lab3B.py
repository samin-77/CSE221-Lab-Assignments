import sys
 
def solve():
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield int(word)
 
    input_gen = get_input()
    try:
        n = next(input_gen)
    except StopIteration:
        return
 
    arr = []
    for _ in range(n):
        arr.append(next(input_gen))
 
    count = 0
    
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width - 1, n - 1)
            right = min(i + 2 * width - 1, n - 1)
            
            if mid < right:
                squares = sorted([arr[k] * arr[k] for k in range(mid + 1, right + 1)])
                j = 0
                for k in range(left, mid + 1):
                    while j < len(squares) and arr[k] > squares[j]:
                        j += 1
                    count += j
                
                l_part = arr[left:mid+1]
                r_part = arr[mid+1:right+1]
                li = ri = 0
                for k in range(left, right + 1):
                    if li < len(l_part) and (ri >= len(r_part) or l_part[li] <= r_part[ri]):
                        arr[k] = l_part[li]
                        li += 1
                    else:
                        arr[k] = r_part[ri]
                        ri += 1
        width *= 2
 
    sys.stdout.write(str(count) + '\n')
 
if __name__ == "__main__":
    solve()