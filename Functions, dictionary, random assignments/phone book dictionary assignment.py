import time

#Initializng the phon book dicrtionary
phoneBook = {"Abhi":9757455821, "Sibi":9758421652, "Subi":8574692514, "Ben": 7025217574}

choice = 1

#function to display menu
def displayMenu():
    global choice
    print("MENU:\n1 -> List all contacts\n2 -> Add a new contact\n3 -> Delete a contact\n4 -> Search a contact\n5 -> Search a contact with number\n6 -> Exit")
    choice = int(input("Enter your choice: "))

#function to list contacts in ascending order
def listContacts():
    for i in sorted(phoneBook.keys()):
        print(i,':',phoneBook[i])
    return

#function to add contact
def addContact():
    key = input("Enter the name: ")
    val = input("Enter the phone number: ")
    phoneBook[key] = val
    return

#function to delete contact
def deleteContact():
    key = input("Enter the name of contact to be deleted: ")
    del phoneBook[key]
    return

#function to search by name
def searchByName():
    key = input("Enter the name: ")
    print(key, ':', phoneBook[key])
    return

#function to search by number
def searchByNumber():
    num = int(input("Enter the number: "))
    for i in phoneBook:
        if phoneBook[i] == num:
            print(i)
            return
    print("number not in phone book")
    return


while(choice!=6):
    displayMenu()
    if choice==1:
        listContacts()
    elif choice==2:
        addContact()
    elif choice==3:
        deleteContact()
    elif choice==4:
        searchByName()
    elif choice==5:
        searchByNumber()
    elif choice==6:
        print("Exited!")
        break
    else:
        print("Wrong choice")
    print("\nDisplaying Menu...")
    time.sleep(3)
    displayMenu()