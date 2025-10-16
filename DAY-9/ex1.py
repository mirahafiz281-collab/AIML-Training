#Write a function to check a number is odd or even
def check_odd_even(number):
    if(number%2==0):
        print('Even Number')
    else:
        print('Odd Number')

given_number=int(input('Enter Number: '))
check_odd_even(given_number)