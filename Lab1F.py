n = int(input())
a = list(map(int, input().split()))

while True:
    changed = False

    for i in range(n - 1):
        if (a[i] % 2) == (a[i + 1] % 2):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True
    if not changed:
        break

print(*a)
