import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    in_order = list(map(int, input_data[1:n+1]))
    pre_order = list(map(int, input_data[n+1:2*n+1]))
    
    in_map = {val: i for i, val in enumerate(in_order)}
    pre_idx = 0
    post_order = []
 
    def build_post_order(in_left, in_right):
        nonlocal pre_idx
        if in_left > in_right:
            return
        
        root_val = pre_order[pre_idx]
        pre_idx += 1
        
        root_in_idx = in_map[root_val]
        
        build_post_order(in_left, root_in_idx - 1)
        build_post_order(root_in_idx + 1, in_right)
        
        post_order.append(root_val)
 
    build_post_order(0, n - 1)
    print(*(post_order))
 
if __name__ == "__main__":
    solve()