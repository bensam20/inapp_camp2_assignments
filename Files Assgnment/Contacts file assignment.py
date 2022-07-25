#function to display menu
def displayMenu():
    global choice
    print("MENU:\n1 -> List all contacts\n2 -> Add a new contact\n3 -> Delete a contact\n4 -> Search a contact\n5 -> Search a contact with number\n6 -> Exit")
    choice = int(input("Enter your choice: "))
    return

#function to list contacts in ascending order
def listContacts():
    phfile = open("phoneBookFile.txt","r")
    pbContents = phfile.readlines()
    for i in sorted(pbContents):
        print(i)
    phfile.close()
    return


#function to add contact
def addContact():
    name = input("Enter the name: ")
    phNum = input("Enter the phone number: ")
    phfile = open("phoneBookFile.txt","a")
    phfile.write(f"{name}:{phNum}\n")
    phfile.close()
    return

#function to search by name
def searchByName():
    phfile = open("phoneBookFile.txt","r")
    pbContacts = phfile.readlines()
    phfile.close()
    searchName = input("Enter the name of contact: ")
    names = []
    for contact in pbContacts:
        names.append(contact.split("\n")[0].split(":")[0])
    if searchName in names:
        entry = pbContacts[names.index(searchName)].split("\n")[0].split(":")
        print(f"Name : {entry[0]} \nNumber : {entry[1]}")
    else:
        print("Contact not found in directory!")
    return


def searchByNumber():
    phfile = open("phoneBookFile.txt","r")
    pbContacts = phfile.readlines()
    phfile.close()
    searchNumber = input("Enter the number of contact: ")
    numbers = []
    for contact in pbContacts:
        numbers.append(contact.split("\n")[0].split(":")[1])
    if searchNumber in numbers:
        entry = pbContacts[numbers.index(searchNumber)].split("\n")[0].split(":")
        print(f"Name : {entry[0]} \nNumber : {entry[1]}")
    else:
        print("Contact not found in directory!")
    return

def deleteContact():
    phfile = open("phoneBookFile.txt", "r")
    pbContacts = phfile.readlines()
    phfile.close()
    phfile = open("phoneBookFile.txt", "w")
    name = input("Enter name of contact to delete : ")
    for contact in pbContacts:
        entry = contact.split("\n")[0].split(":")
        if entry[0] != name:
            phfile.write(f"{contact}")
    phfile.close()

choice = 1
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
    displayMenu()

