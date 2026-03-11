# num = 123
# a = num % 10  # a = 3
# num = num // 10   #num = 12
# b = num % 10  # b = 2
# c = num // 10 # num = 1
# rev = a*100 + b*10 + c*1  # 300 + 20 + 1 = 321
# print(rev)

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number:", reverse)


