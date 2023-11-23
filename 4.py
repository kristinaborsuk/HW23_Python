n = int(input("Enter your number: "))
while (n < 1) or (n > 9):
    print("Incorrect input. Try again:")
    n = int(input("Enter your number: "))


# while-loop solution
print("While-loop solution:")
counter = 1
while counter <= 10:
    print(f"{counter} x {n}: {counter * n}")
    counter += 1


print("For-loop solution:")
# for-loop solution
for counter in range(1, 10 + 1):
    print(f"{counter} x {n}: {counter * n}")