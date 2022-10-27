# This is a health management software that logs food and exercise of three people and store it in text files.
print("This is a health management software, that can be used to track the food and exercise schedule of three people.")


def main():
    n = int(input("Enter:\n\t1 to read files\n\t2 to write files\nEnter your Choice: "))
    if n == 1:
        read()
    elif n == 2:
        write()
    else:
        print("invalid choice")
        main()


def write():
    n = int(input(
        "Enter:\n\t1 for Harry\n\t2 for Rohan\n\t3 for Hammad\nEnter your Choice: "))
    if n == 1:
        harryWrite()
    elif n == 2:
        rohanWrite()
    elif n == 3:
        hammadWrite()
    else:
        print("Invalid Choice")
        write()


def read():
    n = int(input("Enter:\n\t1 for Harry\n\t2 for Rohan\n\t3 for Hammad\nEnter your Choice: "))
    if n == 1:
        harryRead()
    elif n == 2:
        rohanRead()
    elif n == 3:
        hammadRead()
    else:
        print("Invalid Choice")
        write()

def harryWrite():
    print("\nWriting in Harry's file")
    n = int(input("Enter:\n\t1 to log food\n\t2 to log Exercise\nEnter your Choice: "))
    if n == 1:
        entry = input("Enter the Food eaten:\n\t")
        with open('D:\Software Development\Python\Projects\HMS\harry\Food.txt', 'a+') as file:
            file.write(entry + "\n")
    elif n == 2:
        entry = input("Enter the Food eaten:\n\t")
        with open('D:\Software Development\Python\Projects\HMS\harry\Exercise.txt', 'a+') as file:
            file.write(entry + "\n")
    else:
        print("Invalid")
        harryWrite()

    
def rohanWrite():
    print("\nWriting in Rohan's file")
    n = int (input("Enter:\n\t1 to log food\n\t2 to log Exercise\nEnter your Choice: "))
    if n == 1:
        entry = input("Enter the Food eaten:\n\t")
        with open('D:\Software Development\Python\Projects\HMS\\rohan\Food.txt', 'a+') as file:
            file.write(entry + "\n")
    elif n == 2:
        entry = input("Enter the Food eaten:\n\t")
        with open('D:\Software Development\Python\Projects\HMS\\rohan\Exercise.txt', 'a+') as file:
            file.write(entry + "\n")
    else:
        print("Invalid")
        rohanWrite()


def hammadWrite():
    print("\nWriting in Hammad's file")
    n = int (input("Enter:\n\t1 to log food\n\t2 to log Exercise\nEnter your Choice: "))
    if n == 1:
        entry = input("Enter the Food eaten:\n\t")
        with open('D:\Software Development\Python\Projects\HMS\hammad\Food.txt', 'a+') as file:
            file.write(entry + "\n")
    elif n == 2:
        entry = input("Enter the Food eaten:\n\t")
        with open('D:\Software Development\Python\Projects\HMS\hammad\Exercise.txt', 'a+') as file:
            file.write(entry + "\n")
        print("Invalid")
        hammadWrite()


def harryRead():
    print("\nReading harry's file")
    n = int (input("Enter:\n\t1 to read food\n\t2 to read Exercise\nEnter your Choice: "))
    try:
        if n == 1:
            with open('D:\Software Development\Python\Projects\HMS\harry\Food.txt') as file:
                content = file.read()
                print(content)
        elif n == 2:
            with open('D:\Software Development\Python\Projects\HMS\harry\Exercise.txt') as file:
                content = file.read()
                print(content)
    except Exception as e:
        print(e)


def rohanRead():
    print("\nReading rohan's file")
    n = int (input("Enter:\n\t1 to read food\n\t2 to read Exercise\nEnter your Choice: "))
    try:
        if n == 1:
            with open('D:\Software Development\Python\Projects\HMS\rohan\Food.txt') as file:
                content = file.read()
                print(content)
        elif n == 2:
            with open('D:\Software Development\Python\Projects\HMS\rohan\Exercise.txt') as file:
                content = file.read()
                print(content)
    except Exception as e:
        print(e)

def hammadRead():
    print("\nReading Hammad's file")
    n = int (input("Enter:\n\t1 to read food\n\t2 to read Exercise\nEnter your Choice: "))
    try:
        if n == 1:
            with open('D:\Software Development\Python\Projects\HMS\hammad\Food.txt') as file:
                content = file.read()
                print(content)
        elif n == 2:
            with open('D:\Software Development\Python\Projects\HMS\hammad\Exercise.txt') as file:
                content = file.read()
                print(content)
    except Exception as e:
        print(e)

try:
    main()
except Exception as e:
    print(e)