#using if-elif-else

monthNo = int(input(('Enter the month number of your dob : ')))

if (monthNo==1):
    print('Personality: Bold and Alert\nBirth Stone: Garnet')
elif (monthNo==2):
    print('Personality: Lucky and Loyal\nBirth Stone: Amethyst')
elif (monthNo==3):
    print('Personality: Naughty and Genius\nBirth Stone: Aquamarine')
elif (monthNo==4):
    print('Personality: Caring and Strong\nBirth Stone: Diamond')
elif (monthNo==5):
    print('Personality: Loving and Practical\nBirth Stone: Emerald')
elif (monthNo==6):
    print('Personality: Romantic and Curious\nBirth Stone: Alexandrite')
elif (monthNo==7):
    print('Personality: Adventurous and Honest\nBirth Stone: Ruby')
elif (monthNo==8):
    print('Personality: Active and Hardworking\nBirth Stone: Peridot')
elif (monthNo==9):
    print('Personality: Sensitive and Pretty\nBirth Stone: Sapphire')
elif (monthNo==10):
    print('Personality: Stylish and Friendly\nBirth Stone: Tourmaline')
elif (monthNo==11):
    print('Personality: Nice and Creative\nBirth Stone: Citrine')
elif (monthNo==12):
    print('Personality: Confident and Freedom loving\nBirth Stone: Zicron')
else:
    print("Wrong month number!")



#using match case
num = int(input(('Enter the month number of your dob : ')))
def month(num):
    match num:
        case 1:
            return "Personality: Bold and Alert\nBirth Stone: Garnet"
        case 2:
            return'Personality: Lucky and Loyal\nBirth Stone: Amethyst'
        case 3:
            return'Personality: Naughty and Genius\nBirth Stone: Aquamarine'
        case 4:
            return'Personality: Caring and Strong\nBirth Stone: Diamond'
        case 5:
            return'Personality: Loving and Practical\nBirth Stone: Emerald'
        case 6:
            return'Personality: Romantic and Curious\nBirth Stone: Alexandrite'
        case 7:
            return'Personality: Adventurous and Honest\nBirth Stone: Ruby'
        case 8:
            return'Personality: Active and Hardworking\nBirth Stone: Peridot'
        case 9:
            return'Personality: Sensitive and Pretty\nBirth Stone: Sapphire'
        case 10:
            return'Personality: Stylish and Friendly\nBirth Stone: Tourmaline'
        case 11:
            return'Personality: Nice and Creative\nBirth Stone: Citrine'
        case 12:
            return'Personality: Confident and Freedom loving\nBirth Stone: Zicron'
        case _:
            return'Wrong month number'
print(month(num))