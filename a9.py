# 1]
# import re 
# var = "gasgg54@#vscsd!s*"
# count = 0
# for i in var:
#     z = ord(i)
#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count += 1
# print(count)

#2]Same Number In Arrays
# arr1 = list(map(int, input("Enter numbers: ").split()))
# arr2 = list(map(int, input("Enter numbers: ").split()))
# arr3 = list(map(int, input("Enter numbers: ").split()))

# for i in arr1:
#     if i in arr2 and i in arr3:
#         print(i)


# Move zeros to then End
# arr = [0,1,0,3,12]
# for i in arr:
#     if i == 0:
#         arr.remove(i)
#         arr.append(i)
# print(arr)    

# 3]Second Largest Element In Array 
# arr = [2,34,5, 67]

# arr.sort()
# print(arr)
# print(arr[-2])

# N = int(input())
# sum = 0
# myList = []
# for i in range(N):
#     a = int(input("Enter Element Value = "))
#     myList.append(a)
# for j in range(len(myList)):
#     if j+1 in range (len(myList)):
#         sum += abs(myList[j])
L = int(input()) 
N = int(input())    

for i in range(N):
    W, H = map(int,input().split())

    if W < L or H < L:
        print("Upload Another")
    elif W >= L and H >= L:
        if W == L and H == L:
            print("Accepted")
        else:
            print("Crop It")