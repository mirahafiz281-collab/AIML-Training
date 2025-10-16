# #Function Lambda
# def add(a,b):
#     total= a+b
#     return total

# result=add(12,15)
# print(result)

#Lambda
# addition = lambda a, b: a + b #kalau kita tentukan nombor terus: print(add(2,3))
# multi = lambda a, b: a*b
# div = lambda a, b: a/b
# avg = lambda a, b: (a+b)/2
# sub = lambda a, b: (a-b)

# num1=int(input('Enter first number:\t'))
# num2=int(input('Enter second number:\t'))

# print('Multiplication result: ', multi(num1,num2))
# print('Subtraction result: ', sub(num1,num2))

#lambda example to find out odd or even number
check_odd= lambda n:"Odd Number" if n%2==1 else 'Even Number'
num1=int(input('Enter Number to check Odd or Even: \t'))
print(check_odd(num1))

