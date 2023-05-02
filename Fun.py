#Converter
while True:
    try:
        a = int(input("""

        1 NUMBER TO CHARACTER
        2 CHARACTER TO NUMBER

     --> """))
        if a == 0:
            break
        elif a == 1:
            nb = int(input("Enter Number Here: "))
            print("ACSII Character--> ",chr(nb))
        elif a == 2:
            nc = input("Enter Char: ")
            if nc[0]=="#":
                print("This is a Comment: ","#",nc)
            else:
                print("ASCII Number--> ",ord(nc))

    except Exception as e:
        print(e)

    