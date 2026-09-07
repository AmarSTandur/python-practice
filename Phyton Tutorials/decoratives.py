# def f():
#     print("First function")
# def function_validation(f):
#     print("second function")
#     def a():
#         print("Third function")
#     e=[a]
#     e[0]()
  
# l=[f]
# l[0]()



# def decorative_func(func):
#     def wrapper():
#         print("Namaskara")
#         func()
#         print("Take care")
#     return wrapper


# @decorative_func
# def intro():
#     print("I Am Amar")



# @decorative_func
# def abc():
#     print("hiiii")
# abc()




# def show_result(result):
#     def abc(a,b):
#         print("Result: ",end="")
#         result(a,b)
#     return abc

# @show_result
# def add(a,b):
#     print(a+b)

# add(2,3)

# @show_result
# def sub(a,b):
#     print(a-b)

# sub(2,5)


# def logger(func):
#     def wrapper(a,b):
#         print(f"Function '{func.__name__}' is being called.")
#         func(a,b)
#     return wrapper

# @logger
# def add(a,b):
#     print(a+b)


# @logger
# def sub(a,b):
#     print(a-b)

# sub(2,5)
# add(2,5)



 


def login_required(func):
    def wrapper():
        print("Checking if user is logged in...")
        func()
    print(wrapper)

@login_required
def view_profile():
    print("Ravi's profile opened.")

view_profile()