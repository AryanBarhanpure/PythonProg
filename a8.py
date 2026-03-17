# # 1]
# fruit_list1= ['apple','berry','cherry','papaya']
# fruit_list2= fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]='guava'
# fruit_list3[1]='kiwi'

# sum=0
# for ls in (fruit_list1,fruit_list2, fruit_list3):
#     if ls[0]=='guava':
#         sum+= 1
#     if ls[1]=='kiwi':
#         sum+= 20
# print(sum)

# 2]
# def f(i, values = []):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)

# 3]
# def func(value, values):
#     var = 1
#     values[0] = 44   # [44,2,3]

# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])

# 4]
# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):  # Character Wise Sort
#     print(dict[_])

# 5]
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
    
# addone("Apple")
# addone("Banana")
# addone("apple")
# print(len(fruit))

# 5]
# arr = [1,2,3,4]

# prod = 0
# for i in range(arr):
#     value = i
#     if value == i:
#         continue
#     i = i + 1
#     while i < arr.length():
#         prod = prod * arr[i]
#         i = i + 1
#     arr.append(prod)

# while i < arr.length():

# for i in range(arr):
    
#     while i < arr.length():
#         value = i
#         if value == i:

#             prod = prod * arr[i]

# 6] product of array without Itself

# def a1(nums):
#     arr = []
#     for i in range(len(nums)):
#         prod = 1
#         for j in range(len(nums)):
#             if i != j:
#                 prod = prod * nums[j]
#         arr.append(prod)
#     print(arr)

# nums = [1,2,3,4]
# a1(nums)
