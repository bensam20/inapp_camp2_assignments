from optparse import Option
import random as r

def numberGuessGame():
    compNum = r.randrange(1,11)
    print(compNum)
    print("I\'ve already guessed one")
    i=0

    while i<5:
        userNum = int(input("Enter your guess: "))
        if userNum not in range(1,11):
            print("Please enter a number between 1 and 10")
            i-=1
            continue
        diff = abs(userNum - compNum)
        if diff in [9,8]:
            res = "very cold"
        elif diff in [7,6]:
            res = "cold"
        elif diff in [5,4]:
            res = "neutral"
        elif diff == 3:
            res = "warm"
        elif diff == 2:
            res = "hot"
        elif diff == 0:
            print("Its a match! Congrats")
            break       
        if userNum < compNum:
            print(f'Your guess is cold from left and {res} from right. Try again')
        else:
            print(f'Your guess is {res} from left and cold from right. Try again')
        i+=1
    return

def startGame():
    print("Menu\n1 -> Start the Game\n2 -> Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        numberGuessGame()
    option = int(input("1 -> Play again\n2 -> Exit\nEnter your choice:"))
    if option == 1:
        startGame()

startGame()