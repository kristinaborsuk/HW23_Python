a = int(input("Type A-number: "))
b = int(input("Type B-number: "))

while (a > b) or (a < 0) or (b < 0):
    print("Incorrect input. Try again:")
    a = int(input("Type A-number: "))
    b = int(input("Type B-number: "))


result = 1
for i in range(a, b+1):
    if (i % 2 == 0) and (i % 3 == 0):
        result *= i

print(result)