# class Human:
#     def __init__(self,name,age):
#         print("constructor called",name)
#         self.name=name
#         self.age=age
#     def walk(self):
#         print(f"{self.name} is walking.his age is {self.age} ")

# human1=Human("Alice",33)
# human1.walk()
# h1=Human("Bob",25)
# h1.walk()




# class Human:
  
#     def __init__(self,name,age):
#         print("constructor called",name)
#         self.name = name 
#         self.age = age
#     def walk(self):
#         print(f"{self.name} is walking.his age is {self.age} ")


# c=Human("John",30)
# print(c.name)
# d=Human("Doe",25)

# print(c.name)
# Human.walk(c)
# c.walk()




# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def show_info(self):
#         print(f"Laptop Brand: {self.brand}, Price: ₹{self.price}")

# laptop1 = Laptop("Dell", 45000)
# laptop2 = Laptop("HP", 55000)

# laptop1.show_info()
# laptop2.show_info()





class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Python Programming")
book2 = Book("Machine Learning", "Andrew Ng")

book1.show_book()
book2.show_book()