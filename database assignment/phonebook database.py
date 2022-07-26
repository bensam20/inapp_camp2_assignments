import pyodbc

#Connecting with the server
conn = pyodbc.connect('''
    Driver={SQL Server};
    Server=DESKTOP-CSCIVVL\SQLEXPRESS;
    Database=phonebook;
    Trusted_Connection=yes;
''')
cursor = conn.cursor()

#creating the phone book table and inserting some values
def initialize():
    try:
        cursor.execute('''
            CREATE TABLE PhBook(
            Name VARCHAR(50),
            PhNumber INT
        );
        ''')
    except Exception as e:
        print(type(e).__name__)

    conn.commit()

def displayMenu():
    global choice
    print("MENU:\n1 -> List all contacts\n2 -> Add a new contact\n3 -> Delete a contact\n4 -> Search a contact\n5 -> Search a contact with number\n6 -> Exit")
    choice = int(input("Enter your choice: "))
    return

#function to display contents in ascending order
def listContacts():
    try:
        cursor.execute('''
            SELECT * FROM PhBook 
            ORDER BY Name;
        ''')
        for name,number in cursor.fetchall():
            print(name,':',number)
    except Exception as e:
        print(type(e).__name__)

#function to add a contact
def addContact():
    name = input("Enter the name: ")
    number = input("Enter the phone number: ")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO PhBook VALUES (?, ?);'''
            ,(name,number)
        )
    except Exception as e:
        print(type(e).__name__)
    conn.commit()

#function to add a contact
def deleteContact():
    name = input("Enter the name to be deleted: ")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM PhBook
            WHERE Name=(?);'''
            ,(name)
        )
    except Exception as e:
        print(type(e).__name__)
    conn.commit()

#Function to search by a name
def searchByName():
    name = input("Enter the name: ")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Name,PhNumber
            FROM PhBook
            WHERE Name=(?);'''
            ,(name)
        )
        for name,number in cursor.fetchall():
            print (name,':',number)
    except Exception as e:
        print(type(e).__name__)

#Function to search by a number
def searchByNumber():
    number = input("Enter the phone number: ")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Name,PhNumber
            FROM PhBook
            WHERE PhNumber=(?);'''
            ,(number)
        )
        for name,number in cursor.fetchall():
            print (name,':',number)
    except Exception as e:
        print(type(e).__name__)


#initialize()
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
    print("\nDisplaying Menu...")
    displayMenu()
conn.close()