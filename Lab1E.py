import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

if n <= 2:
    if all(a[i] <= a[i+1] for i in range(n-1)):
        print("YES")
        print(0)
    else:
        print("NO")
    sys.exit()
b = sorted(a)
pos_even = {}
pos_odd = {}

for i, v in enumerate(a):
    if i % 2 == 0:
        pos_even.setdefault(v, 0)
        pos_even[v] += 1
    else:
        pos_odd.setdefault(v, 0)
        pos_odd[v] += 1

for i, v in enumerate(b):
    if i % 2 == 0:
        if pos_even.get(v, 0) == 0:
            print("NO")
            sys.exit()
        pos_even[v] -= 1
    else:
        if pos_odd.get(v, 0) == 0:
            print("NO")
            sys.exit()
        pos_odd[v] -= 1
ops = []
for i in range(n - 2):
    for j in range(n - 2):
        if a[j] > a[j + 2]:
            a[j], a[j+1], a[j+2] = a[j+2], a[j+1], a[j]
            ops.append((j + 1, j + 3))

print("YES")
print(len(ops))
for l, r in ops:
    print(l, r)
