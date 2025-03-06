#using a stack to implement a library management system with crud operations
top = 0    #initialise top of stack
library = [[], [], []]    #creating an empty stack, with each element containing 3 pieces of information

def create():    #create function
    global top, library
    id = int(input("Enter book ID: "))
    if top > 0:
        for i in range(top):
            if library[i][0] == id:    #verifying if ID already exists
                print("Book ID already exists! Please use update function or a new ID.")
                return 1
    library[top].append(id)
    library[top].append(input("Enter book name: "))
    library[top].append(input("Enter author's name: "))
    print("Successfully created!")
    top += 1
    return 1

def read():
    global top, library
    if top == 0:    #empty library error
        print("Library empty!")
        return 0
    record = input("Do you wish to view all records (A) or a specific record (S): ")    #asking user to read single or multiple records
    if record == "A" or record == "a":
        for i in range(top):
            print("Book ID:", library[i][0], "    Book Name:", library[i][1], "    Book Author:", library[i][2])
        print("All records displayed.")
        return 1
    elif record == "S" or record == "s":
        id = int(input("Enter book ID: "))
        for i in range(top):
            if library[i][0] == id:
                print("Book ID:", library[i][0], "    Book Name:", library[i][1], "    Book Author:", library[i][2])
                print("Record displayed.")
                return 1
            print("Record not found!")    #incorrect ID error
            return 0
    else:    #incorrect input error
        print("Incorrect input!")
        return 0


def update():
    global top, library
    id = int(input("Enter book ID: "))
    for i in range(top):    #searching for given ID in library
        if library[i][0] == id:
            library[i][0] = int(input("Enter new book ID: "))
            library[i][1] = input("Enter new book name: ")
            library[i][2] = input("Enter new author's name: ")
            print("Successfully updated!")
            return 1
        print("Record does not exist! Please use create function or an existing ID.")    #new ID error
        return 0

def delete():
    global top, library
    if top == 0:    #empty library error
        print("Library empty!")
        return 0
    id = int(input("Enter book ID: "))
    for i in range(top+1):
        if library[i][0] == id:    #ID found
            for j in range(i, top+1):
                library[j][0] = library[j+1][0]
                library[j][1] = library[j+1][1]
                library[j][2] = library[j+1][2]
            top -= 1
            return 1
        print("Record not found!")    #ID does not exist error
        return 0

def menu():    #creating menu
    global top, library
    print("Create (C)    Read (R)    Update (U)    Delete(D)")
    u = input("Select an option: ")
    if u == "C" or u == "c":
        create()
    elif u == "R" or u == "r":
        read()
    elif u == "U" or u == "u":
        update()
    elif u == "D" or u == "d":
        delete()
    else:    #incorrect input error
        print("Incorrect input!")
        print("Program Terminated.")
        exit()
    cont = input("Do you wish to continue? ")
    if cont == "Y" or cont == "y":
        menu()
    elif cont == "N" or cont == "n":
        print("Program Terminated.")
        exit()
    else:    #incorrect input error
        print("Incorrect Input.")
        print("Program Terminated.")
        exit()

#main function
menu()
