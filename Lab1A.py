T = int(input())
for _ in range(T):
    nums = int(input())
    if nums % 2 == 0:
        print(nums, " is an Even number.")
    elif nums % 2 != 0:
        print(nums, " is an Odd number.")