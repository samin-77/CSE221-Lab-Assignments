t = int(input())
for _ in range(t):
    n = int(input())
    ids = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    students = []
    for i in range(n):
        students.append([ids[i], marks[i]])
    swaps = 0
    for i in range(n):
        best_idx = i
        for j in range(i + 1, n):
            if students[j][1] > students[best_idx][1]:
                best_idx = j
            elif students[j][1] == students[best_idx][1]:
                if students[j][0] < students[best_idx][0]:
                    best_idx = j
        if best_idx != i:
            students[i], students[best_idx] = students[best_idx], students[i]
            swaps += 1
    print(f"Minimum swaps: {swaps}")
    for sid, mark in students:
        print(f"ID: {sid} Mark: {mark}");
