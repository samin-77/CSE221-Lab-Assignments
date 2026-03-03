import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    ptr = 0
    while ptr < len(input_data):
        n = int(input_data[ptr])
        in_order = input_data[ptr+1 : ptr+1+n]
        post_order = input_data[ptr+1+n : ptr+1+2*n]
        ptr += 1 + 2*n
        
        in_map = {val: i for i, val in enumerate(in_order)}
        post_ptr = n - 1
        res = []
 
        def build(l, r):
            nonlocal post_ptr
            if l > r: return
            root_val = post_order[post_ptr]
            post_ptr -= 1
            idx = in_map[root_val]
           
            right_res = build(idx + 1, r)
            left_res = build(l, idx - 1)
            return [root_val] + (left_res if left_res else []) + (right_res if right_res else [])
 
        final_res = build(0, n - 1)
        print(*(final_res))
 
solve()
