#LISTS

#Question 1
myList=[25,10,15,30,20]
myList.sort()
print(myList[0])

#Question 2
myList=[25,10,15,30,20]
myList.sort()
print(myList[1])

#Question 3
numList=[1,2,3,4,5,6,7,8,9,10]
numListEven=[]
numListOdd=[]
for i in numList:
    if i%2==0:
        numListEven.append(i)
    else:
        numListOdd.append(i)
print('Odd numbers: ',numListOdd)
print('Even numbers: ',numListEven)

#Question 4
myList=[25,10,15,30,20]
myList.reverse()
print(myList)

#Question 5
for i in range(1,50):
    if(i%2!=0):
        print(i)

#Question 6
numList=[1,2,3,4,5,6,7,8,9,10]
odd=0
even=0
for i in numList:
    if i%2==0:
        even+=1
    else:
        odd+=1
print('Count of odd numbers: ',odd)
print('Count of even numbers: ',even)
