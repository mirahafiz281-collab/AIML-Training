from ourpack import calc
while True: #1.Add While True for choice
    try:
        fnum=float(input('Enter first number: '))
        snum=float(input('Enter Second NUmber: '))
        op=input('Choose operation +,-,*,/: \t')
        if(op=='+'):
            print('Result: \t',calc.add(fnum,snum))
        elif(op=='-'):
            print('Result: \t',calc.sub(fnum,snum))
        elif(op=='*'):
            print('Result: \t',calc.multi(fnum,snum))
        elif(op=='/'):
            print('Result: \t',calc.div(fnum,snum))
        else:
            raise ValueError

    except ZeroDivisionError as ze:
        print('Division by 0 not allowed',ze)
    except ValueError as ve:
        print('Error in values',ve)
    except Exception as ex:
        print('Error!!!',ex)
#2. delete finally here to add choice
    # finally:
    #     print('End of Program')

#3. Add choice 
    choice=input('Do you wanna continue if yes press y').lower()
    if(choice!='y'):
        print('Bye')
        break 
