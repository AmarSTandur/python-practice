# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):   
#     return a*b
# def div(a,b):
#     return a/b 
# print("Simple Calculator")
# print("1.Addition")
# print("2.Subtraction")      
# print("3.Multiplication")
# print("4.Division") 
# print("5.Exit")
# while True:
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         a=int(input("Enter first number: "))
#         b=int(input("Enter second number: "))
#         print("Result:",add(a,b))
#     elif choice==2:
#         a=int(input("Enter first number: "))
#         b=int(input("Enter second number: "))
#         print("Result:",sub(a,b))
#     elif choice==3:
#         a=int(input("Enter first number: "))
#         b=int(input("Enter second number: "))
#         print("Result:",mul(a,b))
#     elif choice==4:
#         a=int(input("Enter first number: "))
#         b=int(input("Enter second number: "))
#         print("Result:",div(a,b))
#     elif choice==5:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.") 


def menu():
    print("Banking System")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
balance=0
while True:
    menu()
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Your balance is:",balance)
    elif choice==2:
        amount=int(input("Enter amount to deposit: "))
        balance+=amount
        print("Amount deposited successfully.")
    elif choice==3:
        amount=int(input("Enter amount to withdraw: "))
        if amount>balance:
            print("Insufficient balance.")
        else:
            balance-=amount
            print("Amount withdrawn successfully.")
    elif choice==4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")