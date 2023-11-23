price = int(input("Enter your price: "))

price_list = [price * weight for weight in range(1, 10+1)]
print(price_list)