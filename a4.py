# // Day3
# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

# // S1
# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

# for i in range(5,0,-1):
#     if i == 3:
#         continue
#     print(i)

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i == 3 and j==3 :
#         continue
#     print(i," ",j)


# i = 1
# while i<=5:
#     print(i)
#     i = i+1

# username = ""
# password = ""
# while username != "admin" and password != "Hello":
#     userName = input("Enter UserName = ")
#     password = input("Enter Password = ")


# n = int(input(" Enter Number = "))
# sum = 0
# i = 1 
# while i<=n:
#     sum = sum+i
#     i=i+1
# print("The Sum Of",n,"Numbers is = ",sum)

# name = input("Enter Name = ")
# name = "Prashant"
# newname = ""
# for i in name:
#     if i not in newname:
#         newname = newname + i
# print(name)     
# print(newname)

# # print(name[::-1])  # reverse String

# rev = ""   # Reverse String
# for i in name:
#     rev = i + rev
# print(rev)

# Palindrome Or Not
# name = input("Enter a string: ")
# reverse = name[::-1]
# if name == reverse:
#     print("The string is Palindrome")
# else:
#     print("The string is not Palindrome")

# Anagram
# name2 = input("Enter a string 1: ")
# name3 = input("Enter a string 2: ")
# count1 = 0
# for i in name2:
#     count1 = count1 + 1
# # print(count1)    

# count2 = 0
# for i in name3:
#     count2 = count2 + 1
# # print(count2)    

# if count1 == count2 : 
#     print("The Number Is Annagram")
# else:
#     print("the Number Is Not Aangram")

# Nested For Loop 
# for i in range(1,4):    #Loop => Rows
#     for j in range(1,4):  #Loop => Columns
#         print(i , end=" ")
#     print()  

# n = int(input("Enter The Numbers of Rows = "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i), end = "") 
#     print()

n = int(input("Enter The Numbers of Rows = "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i, end = "") 
    print()

n = int(input("Enter The Numbers of Rows = "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("+", end = "") 
    print()
