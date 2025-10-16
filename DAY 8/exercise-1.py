# #Take user marks from user with in 0 to 50 
# #if user enter outside [0-50], raise Error InvalidMarks using Custom Exception
# #Give chance to user till, he/she entered valid marks

# class InvalidMarks(Exception):
#     pass

# def check_marks(marks):
#     if(marks<0):
#         raise ValueError ('Marks should not be negative')
#     elif(marks>50):
#         raise InvalidMarks ('Marks should not be with 0 to 50')
#     else:
#         print(f'Marks {marks} is accepted!')

# while True:
#     try:
#         userMarks=int(input('Enter your Marks [0-50]: ') )
#         check_marks(userMarks)
#     except InvalidMarks as e:
#         print('Invalid Marks: ',e)
#     except Exception as ex:
#         print('Error!!!',ex)
#     else:
#         print('Recorded')
#         break
    
#     choice=input('Do you wanna to re-enter? If yes press y: ').lower()
#     if(choice!='y'):
#         print('Bye')
#         break 

# #Example use packages from ourpack (mark.py)
from ourpack import mark

while True:
    try:
        userMarks=int(input('Enter your Marks [0-50]: ') )
        mark.check_marks(userMarks) #tambah mark.check_marks
    except mark.InvalidMarks as e: #tambah mark.InvalidMarks
        print('Invalid Marks: ',e)
    except Exception as ex:
        print('Error!!!',ex)
    else:
        print('Recorded')
        break
    choice=input('Do you wanna to re-enter? If yes press y: ').lower()
    if(choice!='y'):
        print('Bye')
        break 
    