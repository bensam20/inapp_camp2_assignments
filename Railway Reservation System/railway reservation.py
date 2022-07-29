import pyodbc

#Connecting with the server
conn = pyodbc.connect('''
    Driver={SQL Server};
    Server=DESKTOP-CSCIVVL\SQLEXPRESS;
    Database=train_db;
    Trusted_Connection=yes;
''')
cursor = conn.cursor()
#Train names in a dictionary:
trains = {1:'TVM_ALP', 2:'TVM_EKM', 3:'TVM_KZK'}


#Finction that receives the destination station and calls the corresponding function
def searchTrain():
    endStn = input("Enter your destination (ALP/ERN/KZK): ")

    if endStn == 'ALP':
        toALP()
    elif endStn == 'EKM':
        toEKM()
    elif endStn == 'KZK':
        toKZK()
    else:
        print("Please enter valid station!")

    
#Function to book ticket and stores in the passengerDetails table 
def bookTicket(trainID, endStation):
    passName = input("Enter Your name: ")
    #inserting a confirmed ticket to the passengerDetails table 
    cursor.execute('''insert into passengerDetails(pass_name,trainID,startStation,endStation,waiting_list) 
                values(?,?,?,?,?);'''
                ,(passName,trainID,1,endStation,0)) 
    print(f"Your ticket is confirmed in {trains[trainID]}")
    conn.commit()
    conn.close()


#Function to book a waiting list ticket
def bookWaitingList(trainID,endStation):
    passName = input("Enter Your name: ")
    #inserting a waiting list ticket into the passengerDetails table
    cursor.execute('''insert into passengerDetails(pass_name,trainID,startStation,endStation,waiting_list) 
                values(?,?,?,?,?);'''
                ,(passName,trainID,1,endStation,1))
    print(f"Your ticket is in waiting list in {trains[trainID]}")
    conn.commit()
    conn.close()


#Function to check availability to go to Alappuzha
def toALP():
    #getting the count of people booked for Alappuzha in TVM_ALP train
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 1;''')
    for i in cursor.fetchall():
        countTrain_1 = i[0]

    #getting the count of people booked for Alappuzha in TVM_EKM train
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 2;''')
    for i in cursor.fetchall():
        countTrain_2 = i[0]

    #getting the count of people booked for Alappuzha in TVM_KZK train
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 3;''')
    for i in cursor.fetchall():
        countTrain_3 = i[0]

    #checks each train for booking availability and confirms the ticket if seat is available
    #if not checks if waiting list is available
    if countTrain_1 < 5:
        bookTicket(1,2)
    elif countTrain_2 < 5:
        bookTicket(2,2)
    elif countTrain_3 < 5:
        bookTicket(3,2)
    else:
        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 1;''')
        for i in cursor.fetchall():
            WLTrain_1 = i[0]

        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 2;''')
        for i in cursor.fetchall():
            WLTrain_2 = i[0]
        
        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 3;''')
        for i in cursor.fetchall():
            WLTrain_3 = i[0]
        
        if WLTrain_1 < 2:
            bookWaitingList(1,2)
        elif WLTrain_2 < 2:
            bookWaitingList(2,2)
        elif WLTrain_3 < 2:
            bookWaitingList(3,2)
        else:
            print("Ticket not available to Alappuzha")
    

#Function to check availability to go to Ernakulam
def toEKM():
    #getting the count of people booked for Ernakulam in TVM_EKM train
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 2;''')
    for i in cursor.fetchall():
        countTrain_2 = i[0]

    #getting the count of people booked for Ernakulam in TVM_KZK train
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 3;''')
    for i in cursor.fetchall():
        countTrain_3 = i[0]

    if countTrain_2 < 5:
        bookTicket(2,3)
    elif countTrain_3 < 5:
        bookTicket(3,3)
    else:
        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 2;''')
        for i in cursor.fetchall():
            WLTrain_2 = i[0]
        
        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 3;''')
        for i in cursor.fetchall():
            WLTrain_3 = i[0]

        if WLTrain_2 < 2:
            bookWaitingList(2,3)
        elif WLTrain_3 < 2:
            bookWaitingList(3,3)
        else:
            print("Ticket not available to Ernakulam")


#Function to check availability to go to Kozhikode
def toKZK():
    #getting the count of people booked for Kozhikode in TVM_KZK train
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 3;''')
    for i in cursor.fetchall():
        countTrain_3 = i[0]

    if countTrain_3 < 5:
        bookTicket(3,4)
    else:
        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 3;''')
        for i in cursor.fetchall():
            WLTrain_3 = i[0]
        
        if WLTrain_3 < 2:
            bookWaitingList(3,4)
        else:
            print("Ticket not available to Kozhikode")

searchTrain()
