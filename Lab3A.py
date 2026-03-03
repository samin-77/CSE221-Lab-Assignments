import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:]]
    
    inversions = 0
 
    def merge_sort(items):
        nonlocal inversions
        if len(items) <= 1:
            return items
        
        mid = len(items) // 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])
        
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += (len(left) - i)
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
 
    sorted_arr = merge_sort(arr)
    
    sys.stdout.write(str(inversions) + '\n')
    sys.stdout.write(' '.join(map(str, sorted_arr)) + '\n')
 
if __name__ == "__main__":
    solve()