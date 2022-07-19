#Question 1
for i in range(2000,2501):
    if(i%5==0):
        if(i%8==0):
            print(i)

#Question 2
num = int(input("Enter the number: "))
for i in range(1,11):
    print(i,'*',num,'=',i*num)