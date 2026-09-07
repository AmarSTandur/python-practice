class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):#getter method
        return self.__name
    def get_age(self):#getter method
        return self.__age
    def set_name(self, name):#setter method
        self.__name = name
    def set_age(self, age):#setter method
        if isinstance(age, int) and age > 0 and age < 100:
            self.__age = age
        else:
            print("Invalid age. Age must be a positive integer less than 100.")
A=Student("Ajay", 2000)

print(A.get_name())
print(A.get_age())
A.set_name("Amar")
A.set_age(2000)       
print(A.get_name())
print(A.get_age())