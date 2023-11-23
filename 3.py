result = 0
for num in range(100, 500):
    result += num
print(f"Sum of ints from 100 to 500 is: {result}")


result = 0
a = int(input("Enter your 'a' number:"))
for num in range(a, 500):
    result += num
print(f"Sum of ints from a to 500 is: {result}")


result = 0
b = int(input("Enter your 'b' number:"))
for num in range(-10, b):
    result += num
print(f"Sum of ints from -10 to b is: {result}")


result = 0
if a > b:
    range_ = range(b, a)
else:
    range_ = range(a, b)

for num in range_:
    result += num
print(f"Sum of ints from a to b is: {result}")