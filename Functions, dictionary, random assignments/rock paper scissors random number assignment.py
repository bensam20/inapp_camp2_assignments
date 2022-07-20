import random


#function for the game
def game():
    i = 0
    userPts=compPts=0
    while i<5:
        print("1 -> ROCK\n2 -> PAPER\n3 -> SCISSORS")
        userChoice = int(input("Enter your choice: "))  #user input the number
        if(userChoice >3 ):
            print("Wrong Choice! Please enter again!")
            continue
        compChoice = random.randrange(1,4)  #computer choosing random number
        print("Computer chooses: ",compChoice)
        #comparing the inputs with the conditions of the game
        if userChoice==1 and compChoice==2:
            compPts+=1
        elif userChoice==3 and compChoice==1:
            compPts+=1
        elif userChoice==2 and compChoice==3:
            compPts+=1
        elif userChoice==1 and compChoice==3:
            userPts+=1
        elif userChoice==2 and compChoice==1:
            userPts+=1
        elif userChoice==3 and compChoice==2:
            userPts+=1
        print("Your Score: ",userPts,"  Computer\'s Score: ",compPts)
        i+=1
    #Comparing the score
    if userPts > compPts:
        print("\n\tCONGRATS! YOU WIN!\n")
    elif userPts < compPts:
        print("\n\tCOMPUTER WINS!")
    else:
        print("\n\tIT\'S A TIE!")
    return

game()








