num = int(input("Num: "))

match num:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("some other number")