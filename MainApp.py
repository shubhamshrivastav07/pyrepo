from OperationsData import save, update,show


def AppRunner():
    print("Welcome The Application !!!")
    op=int(input("Enter Your Choice :\n1 add\n2 update\n3 show\n4 delete\n5 searchById"))
    match(op):
        case 1: save()
        case 2: update()
        case 3: show()
        case _:print("No Option available")
    AppRunner()



AppRunner()



