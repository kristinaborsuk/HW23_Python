a = int(input("Type A-number: "))
b = int(input("Type B-number: "))

while (a > b) or (a < 0) or (b < 0):
    print("Incorrect input. Try again:")
    a = int(input("Type A-number: "))
    b = int(input("Type B-number: "))

result = ''
for i in range(a, b+1):
    counter = 1
    while counter <= i:
        result += str(i)
        counter += 1

print(result)