class InvalidAge(Exception):
    pass #keyword 

def check_age(age):
    if(age<=0):
        raise ValueError('Age should not be negative')
    elif(age<18):
        raise InvalidAge ('Age should be greater than 18 years')
    elif(age>=65):
        raise InvalidAge ('Too old for employement')
    else:
        print(f'Age {age} is accepted and valid age for employement')

try:
    userage=int(input('Enter your age: ') )
    check_age(userage)
except Exception as e:
    print('Invalid Age: ',e)
except Exception as ex:
    print('Error!!!',ex)

