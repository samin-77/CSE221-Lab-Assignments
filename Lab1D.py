import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dec = True
    for i in range(1,n):
        if arr[i] < arr[i-1]:
         dec = False
         break
       
    if dec:
      print("YES")
    elif dec == False:
      print("NO")


