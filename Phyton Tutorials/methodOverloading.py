# class Calculator:

#     def add(self, a, b, c=0):
#         print(a + b + c)
# c = Calculator()
# c.add(5, 10)
# c.add(10, 20, 30)


# #Method Overrriding 
# class Animal:#parent class
#     def make_sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):#child class
#     def make_sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def make_sound(self):
#         print("Cat meows")
# d = Dog()
# d.make_sound()  # Output: Dog barks



#Super() function in method overriding



# class Animal:#parent class
#     def make_sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):#child class
#     def __init__(self, name):
#         self.name = name    
#     def make_sound(self):
#         super().make_sound()  # Call the parent class method
#         print(f"{self.name} bark")  # Child class-specific behavior
#     def get_angry(self):
#         super().make_sound()  # Call the parent class method
#         self.make_sound()  # Call the overridden method
       

# d=Dog("doggy")
# d.make_sound()  # Output: Animal makes a sound
# d.get_angry()  # Output: doggy is angry





# #Abstract class and abstract method

# from abc import ABC, abstractmethod

# class Vehicle(ABC):  # Abstract base class
#     @abstractmethod
#     def start_engine(self):
#         pass  # Abstract method with no implementation

# class Car(Vehicle):
#     def __init__(self,name):
#         self.name=name
#     def start_engine(self):
#         print(f"{self.name} engine started")  # Concrete implementation of the abstract method


# # Usage
# car = Car("Toyota")
# print(car.name)
# car.start_engine()

# # HW
# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#     def display_info(self):
#         print(f"Brand: {self.brand}, Price: ${self.price}")

# m1 = Mobile("Samsung", 20000)
# m2 = Mobile("Apple", 80000)

# m1.display_info()
# m2.display_info()




# # HW
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks  

#     def display_info(self):
#         print(f"Name: {self.name}, has scored {self.marks   }")
# student1 = Student("Alice", 85)
# student2 = Student("Bob", 90)

# student1.display_info()
# student2.display_info()



class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def display_info(self):
        print(f"Title: {self.title}, Rating: {self.rating}")
M1 = Movie("Inception", 8.8)
M2 = Movie("The Dark Knight", 9.0)