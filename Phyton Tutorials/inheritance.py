class Family:
    def __init__(self, surname):
        self.surname = surname

class Child(Family):
    def __init__(self, surname, name):
        super().__init__(surname)
        self.name = name

child = Child("Gowda", "Ajay")
print(f"{child.name} {child.surname}")  # Inherits surname from Family


# class User:
#     def __init__(self, username):
#         self.username = username

#     def login(self):
#         print(f"{self.username} logged in")

# class Admin(User):
#     def delete_user(self, user):
#         print(f"Admin {self.username} deleted user {user}")

# a1= Admin("karnataka_admin")
# a1.login()  # Inherited from User
# a1.delete_user("111")  # Admin-specific method

# a2=Admin("Amar")
# print(a2.username)
# a2.login()
# a2.delete_user("222")