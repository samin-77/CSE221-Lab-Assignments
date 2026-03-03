import sys
from collections import deque
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))
 
    if n == 0:
        return
 
    results = []
    queue = deque([(0, n - 1)])
 
    while queue:
        low, high = queue.popleft()
        if low <= high:
            mid = (low + high) // 2
            results.append(a[mid])
            queue.append((low, mid - 1))
            queue.append((mid + 1, high))
 
    print(*(results))
 
if __name__ == "__main__":
    solve()