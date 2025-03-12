library = []  # Creating an empty stack

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def create():
    id = get_valid_int("Enter book ID: ")
    if any(book[0] == id for book in library):  # Checking for duplicate ID
        print("Book ID already exists! Please use update function or a new ID.")
        return
    if id <= 0:    #Checking for negative ID
        print("Negative ID entered!")
        return
    name = input("Enter book name: ")
    if len(name.strip()) == 0:    #Checking if string is empty
        print("Invalid input! Please enter a book name!")
        return
    author = input("Enter book author: ")
    if len(author.strip()) == 0:    #Checking if string is empty
        print("Please enter book author!")
        return
    library.append([id, name, author])
    print("Successfully created!")

def read():
    if len(library) == 0:  # Empty library error
        print("Library empty!")
        return
    
    record = input("Do you wish to view all records (A) or a specific record (S): ")
    
    if record in ["A", "a"]:
        print("Library Records:")
        print("=" * 60)
        print(f"{'Book ID':<10}| {'Book Name':<20}| {'Author':<20}")
        print("=" * 60)
        for book in library:
            print(f"{book[0]:<10}| {book[1]:<20}| {book[2]:<20}")
        print("=" * 60)
        print("All records displayed.")
    
    elif record in ["S", "s"]:    #Checking if record exists
        id = get_valid_int("Enter book ID: ")
        found = False
        for book in library:
            if book[0] == id:
                print("Record Found:")
                print("=" * 60)
                print(f"{'Book ID':<10}| {'Book Name':<20}| {'Author':<20}")
                print("=" * 60)
                print(f"{book[0]:<10}| {book[1]:<20}| {book[2]:<20}")
                print("=" * 60)
                found = True
                break
        if not found:
            print("Record not found!")
    else:
        print("Incorrect input!")

def update():
    id = get_valid_int("Enter book ID: ")
    for book in library:    #Checking if record exists
        if book[0] == id:
            book[0] = get_valid_int("Enter new book ID: ")  
            book[1] = input("Enter new book name: ")
            book[2] = input("Enter new author's name: ")
            print("Successfully updated!")
            return
    print("Record does not exist! Please use create function or an existing ID.")

def delete():
    if len(library) == 0:  # Empty library error
        print("Library empty!")
        return
    id = get_valid_int("Enter book ID: ")
    for i, book in enumerate(library):
        if book[0] == id:  # ID found
            del library[i]
            print("Record deleted successfully!")
            return
    print("Record not found!")

def menu():  # Creating menu
    print("Create (C)  |  Read (R)  |  Update (U)  |  Delete (D)")
    u = input("Select an option: ")
    if u in ["C", "c"]:
        create()
    elif u in ["R", "r"]:
        read()
    elif u in ["U", "u"]:
        update()
    elif u in ["D", "d"]:
        delete()
    else:  # Incorrect input error
        print("Incorrect input!")
    cont = input("Do you wish to continue? ")
    if cont in ["Y", "y"]:
        menu()
    elif cont in ["N", "n"]:
        print("Program Terminated.")
        exit()
    else:  # Incorrect input error
        print("Incorrect Input.")
        print("Program Terminated.")
        exit()

# Main function
menu()
