# Find divisors
num = int(input("Enter number: "))
print("Divisors:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)