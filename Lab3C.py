import sys
 
def solve():
    
    line = sys.stdin.read().split()
    if not line:
        return
    
    a = int(line[0])
    b = int(line[1])
    mod = 107
    
    res = 1
    a = a % mod
    
    while b > 0:
       
        if b % 2 == 1:
            res = (res * a) % mod
        
        
        a = (a * a) % mod
        b //= 2
        
    print(res)
 
if __name__ == "__main__":
    solve()