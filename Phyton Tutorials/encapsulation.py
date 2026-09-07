class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)




# l=[1, 2, 3, 4, 5]
# l.append
# print(l)









# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password  # Private attribute

#     def get_username(self):
#         return self.username

#     def check_password(self, password):
#         return password == self.__password

# user = User("dev_karnataka", "pass1234")
# print(user.get_username())  # Access allowed
# print(user.check_password("wrong_pass"))  # Returns False
# print(user.check_password("pass1234"))  # Returns True




class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute
    def check_balance(self):
        print(f"Current balance: {self.__balance}")
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

a1=BankAccount("123456789", 1000)
a1.deposit(500)     
a1.withdraw(300)
a1.check_balance()
a2=BankAccount("987654321", 2000)
a2.deposit(1000)
a2.withdraw(500)
a2.check_balance()  

print(a1.account_number)  # Access allowed
print(a2.account_number)  # Access allowed

