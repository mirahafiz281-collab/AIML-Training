import math
import inspect

# num=int(input('Enter Number to find out square root: '))
# print(f'Square root of {num} \t',round(math.sqrt(num),2))

functions = inspect.getmembers(math, inspect.isbuiltin) #function untuk math module
print ('All Function in math module')
for n, func in functions:
    print(n,end="\t")