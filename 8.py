n = int(input("Enter your number: "))
while n <= 0:
    print("Incorrect input. Try again:")
    n = int(input("Enter your number: "))


while n > 0:
    float_part = n % 10
    if float_part == 2:
        print("TRUE")
        break
    n = n // 10
else:
    print("FALSE")