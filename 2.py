num = input("Enter the number: ")
dig_one, dig_two = map(int, num)
if dig_one < dig_two:
    print(f"{dig_two} is bigger!")
else:
    print(f"{dig_one} is bigger!")

if dig_one == dig_two:
    print("Nubers are equal!")
else:
    print("Nubers are non-equal!")