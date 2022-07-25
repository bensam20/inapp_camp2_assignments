#Dictionary to store the record with roll number as the key
studentRecord = {1: ["Abhi",95,94,97,89,95], 2: ["Alan",90,94,85,83,92]}

#function to enter the record
def createRecord():
    rollNum = int(input("Enter the Student Roll Number: "))
    name = input("Enter Student Name: ")
    mathMark = int(input("Enter Marks in Maths: "))
    phyMark = int(input("Enter Marks in Physics: "))
    chemMark = int(input("Enter Marks in Chemistry: "))
    engMark = int(input("Enter Marks in English: "))
    pgmingMark = int(input("Enter Marks in Programming: "))
    detaiList = [name, mathMark,phyMark,chemMark,engMark,pgmingMark]
    studentRecord[rollNum] = detaiList
    return

#function to delete the record
def deleteRecord():
    rollNum = int(input("Enter the Roll Number of the Student to be Deleted: "))
    del studentRecord[rollNum]
    return

#function to modify the record
def modifyRecord():
    createRecord()
    return

#function to display the records
def displayRecord():
    for student in studentRecord:
        print(student, studentRecord[student])
    return

#function to display the record of the given roll number
def displyWithRollnum():
    rollNum = int(input("Enter the Roll Number: "))
    print(studentRecord[rollNum])    
    return

#function that prints the menu
def printMenu():
    print("""Menu
    1 -> Create a Student Record
    2 -> Delete a Student Record
    3 -> Modify Marks of a Student
    4 -> Display all Records
    5 -> Display a Student\'s Record
    6 -> Exit""")
    choice = int(input("Enter your choice: "))
    return choice

#the report card management function
def studentReportCardManagementSystem():
    choice = printMenu()
    while(choice != 6):
        match choice:
            case 1:
                createRecord()
            case 2:
                deleteRecord()
            case 3:
                modifyRecord()
            case 4:
                displayRecord()
            case 5:
                displyWithRollnum()
            case 6:
                break
            case _:
                print("Please enter a valid option")
        choice = printMenu()

studentReportCardManagementSystem()