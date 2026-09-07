class Account:
    def __init__(self,id,holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0.0 #encapsulation

    def check_balance(self):
        print(f"Account ID: {self.id}, Holder: {self.holder_name}, Balance: {self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
            print("Amount deposited successfully.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
            print("Amount withdrawn successfully.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
class SavingsAccount(Account):
    def calculate_interest(self, rate):
        interest = self._balance * (rate / 100)
        self._balance += interest
        print(f"Interest of {interest} added. New balance: {self._balance}")
    
class CurrentAccount(Account):
    def withdraw(self, amount):
        overdraft_limit = 1000
        if amount > 0 and amount <= self._balance + overdraft_limit:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
            print("Amount withdrawn successfully.")
        else:
            print("Invalid withdrawal amount or insufficient balance and it over then overdraft limit.")


class Bank:
    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self, account_type, id, holder_name):
        account_type = account_type.lower()
        if account_type == "savings":
            account = SavingsAccount(id, holder_name)
        elif account_type == "current":
            account = CurrentAccount(id, holder_name)
        else:
            print("Invalid account type.")
            return
        self.__accounts[id] = account
        print(f"{account_type.capitalize()} account created for {holder_name} with ID {id}.")
        return account

    def get_account(self, id):
        return self.__accounts.get(id, None)

b1=Bank("My Bank", "New York")
s1=b1.create_account("savings", "001", "Alice")

c1=b1.create_account("current", "002", "Bob")

s1.deposit( 500)
c1.deposit(1000)

s1.withdraw(200)
c1.withdraw(1500)  # This should be allowed due to overdraft
s1.calculate_interest(5)  # Calculate interest for savings account




