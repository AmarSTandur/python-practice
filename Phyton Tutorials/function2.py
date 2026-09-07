# def add(*numbers):
#     return sum(numbers)

# c=add(1,100,23)
# print(c)



# def student_info(**details):
#     print(details)
#     print(type(details))
#     for key,value in details.items():
#         print(f"{key}:{value}")
# student_info(name="Amar",age=21,course="python")



##lambda function
# add=lambda a,b:a+b
# print(add(1,2))
# double=lambda x:2*x
# print(double(100))




# Student=[
# {"name":"amar","marks":10},
# {"name":"darshan","marks":100},
# {"name":"adarsh","marks":50}
# ]
# Student.sort(key=lambda x:x["marks"], reverse = True)
# print(Student)



# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))




#using for loop
# n=int(input())
# fact=1
# for i in range (1,n+1):
#     fact=fact*i
# print("factorial of ",n,"is",fact)




# def calculate(a,b):
#     def add():
#         print(a+b)
#     def sub():
#         print(a-b)
#     def mul():
#         print(a*b)
#     add()
#     sub()
#     mul()
# calculate(10,2)


