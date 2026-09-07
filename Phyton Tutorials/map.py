# num=[2,3,4,5,6]
# def double(x):
#     return x*2
# res=map(double,num)
# print(list(res))



nums=[1,2,3,4,5]
res=map(lambda x : x*2,nums)
print(list(res))





# #FILTERS

# nums=[1,2,3,4,5]
# def is_even(x):
#     return x%2==0
# res=filter(is_even,nums)
# print(list(res))


# nums=[1,2,3,4,5]
# def is_odd(x):
#     return x%2!=0
# res=filter(is_odd,nums)
# print(list(res))


# nums=[1,2,3,4,5]
# res=filter(lambda x:x%2==0,nums)
# res1=filter(lambda x:x%2!=0,nums)
# print(list(res))
# print(list(res1))







# #REDUCE
# from functools import reduce
# num=[1,2,3,4,5]
# def add(x,y):
#     return x+y
# res = reduce(add,num)
# print(res)




from functools import reduce

scores = [45, 67, 89, 34, 76, 90]

# 1. Increase all scores by 5 using map
updated = list(map(lambda x: x + 5, scores))

# 2. Filter only passing students (>= 50)
passed = list(filter(lambda x: x >= 50, updated))

# 3. Find the total marks of all passed students using reduce
total = reduce(lambda x, y: x + y, passed)

print("Updated Scores:", updated)
print("Passed Students:", passed)
print("Total Marks:", total)