# # // Day 2
# from numpy import append


# myList = ["Aryan","Ayush","Sanjay","Om","Kunal","Prashant","Sushil",77,"Ashish",60.45,"Aman"]

# # print(myList)
# # print(type(myList))
# # print(myList[0])
# # print(myList[1])
# # print(myList[2])
# # print(myList[-1])
# # print(myList[2:5])
# # print(myList[:5])
# # print(myList[1:])
# # print(myList[1:8:2])
# # print(myList[:])
# # print(myList[::-1])

# # append
# # myList.append('harsh')
# # myList.append("Himesh")
# # print(myList)

# # insert
# myList.insert(1,"Salmon")
# print(myList)

# # remove
# myList.remove("Ashish")
# print(myList)

# # New List
# newList = myList.copy() #cloning
# print(myList)
# print(newList)

# # Two Dimesional List
# myList1 = [["Aryan",19],['Harsh',33],["Mac",21]]

# print(myList1)

# print(myList1[0][0])
# print(myList1[0][1])
# print(myList1[1][0])
# print(myList1[2][0])
# print(myList1[2][1])

# # ->  Steps Of Two Dimensional Array
# #     [       0      1
# #        0 ["Aryan",19],
# #        1 ['Harsh',33],
# #        2 ["Mac",21]
# #         ]

# # List Multiply
# list1 = ["Aryan","Om"]
# print(list1*2)

# list2 = [22,12]
# print(list1+list2)

# # Delete List
# myList3 = [50.25,"Aryan","Om"]
# del myList3[2]
# # del myList3    -> Gives Error
# print(myList3)

# myList3.clear()  # To Clear Entire List
# print(myList3)

# name = "Aryan"
# print(name)
# myName = list(name) # Converted To List -> "Type Casting" [String -> List] 
# print(myName)


# myList4 = [44,22,77,0,9,88]   # Should Have Same "Data Type"
# # myList4.sort()  # By Default "Ascending"
# myList4.sort(reverse=True)  # Desending
# print(myList4)

# math = 10
# phy = 10
# print(id(math))  # "id" Function Used to return Address Of variable
# print(id(phy)) # Address Should be Same In Both Cases(Memory Manager In Python assign "Same Address" Because "Same values")

# # Aliasing Concept
# myList5 = [44,22,23,0,9,88] # Changes In One List Changes Another
# newList5 = myList5
# print(id(myList5))
# print(id(newList5))

# # Looping 
# # Special Operator ->  
# # 1]Membership Operator ->  1] in 2] not in
# name1 = "Aryan"
# print("Z" in name)
# print("Z" not in name)

# #Looping
# # for i in range(1,6):
# #     print(i)
# # print()
# # for i in range(6):
# #     print(i)
# # print()
# # for i in range(1 ,10 , 2):  # Increament
# #     print(i)
# # print()
# # for i in range(5 ,0 , -1):  # Increament
# #     print(i)
# # print()
# # for i in range(1,11):  # Increament
# #     print(i*2)
# print()

# Table Vertically
# for i in range(1,11):  # Increament
#     print(i*2 ," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7)

# no = float(input("Enter The Digit = "))
# if no>0:
#     print("Positive")
# if no<0:
#     print("Negative")
# if no==0:
#     print("Zero")

# WAP to accept The Day and Check The Working Days

# no1 = (input("Enter The Day = "))
# myList6 = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# if(no1 == myList6.range(0,7)):  # Wrong
#     print("WeekDay")
# print("WeekEnd")

# days = input("Enter The Day = ")
# if days == "SATURDAY" or "SUNDAY" or "saturday" or"sunday":
#     print("Weekend")
# else:
#     print("Working Days")

# 
# math = int(input("Enter The Maths  = "))
# phy = int(input("Enter The phy = "))
# chem = int(input("Enter The Chem = "))

# total = math + phy + chem
# percentage = ((total*100)/150)

# if percentage>=60:
#     print("You are eligible",percentage)
# else:
#     print("You are not eligible",percentage)

# Wap To Accept

a1 = int(input("Enter The first Value  = "))
a2 = int(input("Enter The Second Value  = "))
a3 = int(input("Enter The Third Value  = "))
a4 = int(input("Enter The Four Value  = "))
a5 = int(input("Enter The Five Value  = "))

# if max(a1,a2,a3,a4,a5):
print(max(a1,a2,a3,a4,a5))
