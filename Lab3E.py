import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    ptr = 1
    results = []
    
    for _ in range(T):
        a = int(input_data[ptr])
        n = int(input_data[ptr+1])
        m = int(input_data[ptr+2])
        ptr += 3
        
        if m == 1:
            results.append(0)
            continue
        
        a %= m
        if a == 0:
            results.append(0)
            continue
        if a == 1:
            results.append(n % m)
            continue
            
        res_sum = 0
        current_a_pow = a
        sum_segment = 1 
        
        temp_n = n
        
        bridge_pow = a
        
        while temp_n > 0:
            if temp_n & 1:
 
                res_sum = (res_sum * bridge_pow + sum_segment * current_a_pow) % m
            
            sum_segment = (sum_segment * (1 + bridge_pow)) % m
            bridge_pow = (bridge_pow * bridge_pow) % m
            temp_n >>= 1
            
        results.append(res_sum)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')
 
if __name__ == "__main__":
    solve()
