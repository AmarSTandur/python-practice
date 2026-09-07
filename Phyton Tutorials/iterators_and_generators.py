# nums=[1,2,3]
# it=iter(nums)
# print(next(it))
# print(next(it)*123)
# print(next(it))


# class CountDown:
#     def __init__(self, start):
#         self.start = start
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start <= 0:
#             raise StopIteration
#         num = self.start
#         self.start -= 1
#         return num

# cd = CountDown(5)

# for i in cd:
#     print(i)



# def f(x):
#     yield x*2

# g=f(5)
# for i in g:
#     print(i)



# def simple_gen(x):
#     for i in range(x):
#         yield i
    
# f=simple_gen()
# for i in f:
#     print(i)

# import sys
# gl=(x*x for x in range(1,101))
# print(type(gl))
# print(sys.getsizeof(gl))
# for i in gl:
#     print(i)



# def infinite_numbers():
#     num = 1
#     while True:
#         yield num
#         num += 1

# gen = infinite_numbers()
# for i in range(5):
#     print(next(gen))


