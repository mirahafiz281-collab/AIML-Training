#Write a program using functions to find greatest of three numbers entered by user.
#Write the solution in assignments folder.

def find_greatest(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

num1=int(input('Enter First Number: '))
num2=int(input('Enter Second number: '))
num3=int(input('Enter third number: '))

greatest=find_greatest(num1, num2, num3)
print(f'The greatest number is = {greatest}')


    