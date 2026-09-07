# class Movie:
#     def __init__(self ,title,rating):
#         self.title=title
#         self.rating=rating

# m1=Movie("Toxic",9.9)
# print(m1.title)
# print(m1.rating)
# m2=Movie("Toxic2",8.5)
# print(m2.title)         
# print(m2.rating)




class Employee:
    def __init__(self,name,designation,salary=100):
        self.name=name
        self.designation=designation
        self.salary=salary
e1=Employee("Alice","Manager",50000)
print(e1.name)  
print(e1.designation)
print(e1.salary)
e2=Employee("Bob","Developer")
print(e2.name)
print(e2.designation)
print(e2.salary)