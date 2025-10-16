# import random
# print ('Random Number from 1 to 1000')
# print(random.randint(1,1000))

import random
name=input('Enter Your name: ')

luckyNumber=random.randint(1,10)
print(f'Mr.\\Ms {name} Cuppon number: {luckyNumber}')
if(luckyNumber==1):
    print('You have won Proton Xl-65 Car')
elif(luckyNumber==4):
    print('You have won an Iphone')
elif(luckyNumber==7):
    print('You have won an Ipad')
else:
    print('Better luck Next Time')