# Find maximum
max_num = float('-inf')
for _ in range(5):
    num = int(input("Enter number: "))
    if num > max_num:
        max_num = num
print("Maximum of the numbers:", max_num)
