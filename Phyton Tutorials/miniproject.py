import random


target=random.randint(1,50)




while True:

    userChoice=input("Guess The Target ot Quit(Q): ")
    if(userChoice=="Q"):
        break


    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice<target):
        print("Yout number was too small. Take a bigger Guess...!!")
    else:
        print("Your number was too big. Take a smallet Guess...!!")


print("-----Game Over-----")