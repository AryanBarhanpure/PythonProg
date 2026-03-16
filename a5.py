stock_entries = int(input("enter The Stock_Entries = "))

stock_prices = []

for  i in range(stock_entries):
    value = int(input(f"Enter {i+1} Price = "))
    stock_prices.append(value)

stock_prices.sort()
print(stock_prices)

smallest = int(input("Enter The smallest Number = "))

final_value = stock_prices[smallest-1]

print(f"The Smallest {smallest} Value is = {final_value}")