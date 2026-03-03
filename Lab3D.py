import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    mod = 10**9 + 7
    
    results = []
    for _ in range(t):
        a11 = int(input_data[ptr])
        a12 = int(input_data[ptr+1])
        a21 = int(input_data[ptr+2])
        a22 = int(input_data[ptr+3])
        x = int(input_data[ptr+4])
        ptr += 5
        
        res = [[1, 0], [0, 1]]
        base = [[a11 % mod, a12 % mod], [a21 % mod, a22 % mod]]
        
        while x > 0:
            if x % 2 == 1:
                
                n11 = (res[0][0] * base[0][0] + res[0][1] * base[1][0]) % mod
                n12 = (res[0][0] * base[0][1] + res[0][1] * base[1][1]) % mod
                n21 = (res[1][0] * base[0][0] + res[1][1] * base[1][0]) % mod
                n22 = (res[1][0] * base[0][1] + res[1][1] * base[1][1]) % mod
                res = [[n11, n12], [n21, n22]]
            
            b11 = (base[0][0] * base[0][0] + base[0][1] * base[1][0]) % mod
            b12 = (base[0][0] * base[0][1] + base[0][1] * base[1][1]) % mod
            b21 = (base[1][0] * base[0][0] + base[1][1] * base[1][0]) % mod
            b22 = (base[1][0] * base[0][1] + base[1][1] * base[1][1]) % mod
            base = [[b11, b12], [b21, b22]]
            x //= 2
            
        results.append(f"{res[0][0]} {res[0][1]}")
        results.append(f"{res[1][0]} {res[1][1]}")
        
    sys.stdout.write("\n".join(results) + "\n")
 
if __name__ == "__main__":
    solve()
