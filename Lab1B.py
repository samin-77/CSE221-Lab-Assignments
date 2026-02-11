T = int(input())
for _ in range(T):
    line = input().split()
    a = float(line[1])
    operator = line[2]
    b = float(line[3])
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    print(result)