# import math
# my_num=int(input('Enter number to find out square root: '))
# print(f'Square root of {my_num} is: ', math.sqrt(my_num))

##Random number
# import random
# print('Your lucky number from 1 to 100 is: ',random.randint(1,100))

#To check function inside module
import math
import inspect

functions = inspect.getmembers(math, inspect.isbuiltin)
for n, func in functions:
    print (n)

#How to check functions in module
print('Sin 90 is: ',math.sin(90))
print('Cos 90 is: ',math.cos(90))
print('Tan 90 is: ',math.tan(90))

deg=int(input('Degree to find out Cos '))
print(f'Cos{deg} is: ',math.cos(deg))