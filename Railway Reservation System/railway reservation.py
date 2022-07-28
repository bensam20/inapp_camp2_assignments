import pyodbc

#Connecting with the server
conn = pyodbc.connect('''
    Driver={SQL Server};
    Server=DESKTOP-CSCIVVL\SQLEXPRESS;
    Database=train_db;
    Trusted_Connection=yes;
''')
cursor = conn.cursor()


def bookTicket():
    startStn = 'TVM'
    endStn = input("Enter your destination (ALP/ERN/KZK): ")
    if endStn == 'ALP':
        toALP()
    elif endStn == 'EKM':
        toEKM()
    elif endStn == 'KZK':
        toKZK()


def bookWaitingList(trainID,endStation):
    passName = input("Enter Your name: ")
    cursor.execute('''insert into passengerDetails(pass_name,trainID,startStation,endStation,waiting_list) 
                values(?,?,?,?,?)'''
                (passName,trainID,'TVM',endStation,1))


def toALP():
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 1;''')
    for i in cursor.fetchall():
        countTrain_1 = i[0]
    if countTrain_1 < 5:
        return
    else:
        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 1;''')
        for i in cursor.fetchall():
            WLTrain_1 = i[0]
        if WLTrain_1 < 2:
            bookWaitingList()
    

def toEKM():
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 2;''')
    for i in cursor.fetchall():
        countTrain_2 = i[0]

    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 2;''')
    for i in cursor.fetchall():
        countTrain_3 = i[0]

    if countTrain_2 < 5:
        return
    
    else:
        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 2;''')
        for i in cursor.fetchall():
            WLTrain_2 = i[0]
        if WLTrain_2 < 2:
            bookWaitingList(2,'EKM')
            return
        else:
            print("Ticket not available to Kohzikode")
    
    
    


def toKZK():
    cursor.execute('''select count(pass_id) from passengerDetails
                                where trainID = 3;''')
    for i in cursor.fetchall():
        countTrain_3 = i[0]
    if countTrain_3 < 5:
        return
    else:
        cursor.execute('''select sum(waiting_list) from passengerDetails
                    where trainID = 3;''')
        for i in cursor.fetchall():
            WLTrain_3 = i[0]
        if WLTrain_3 < 2:
            bookWaitingList(3,'KZK')
            return
        else:
            print("Ticket not available to Kohzikode")

bookTicket()