#def function_name(parameters):
#     *** Docstring***
#      statement(s)

#function without parameters
# def welcome():
#     print("Welcome to Functions")
#     print("Our First function")

# welcome() #nak perkataan welcome sekali sahaja dalam output
# welcome() #tambah ni kalau nak welcome itu dua kali dalam output

#Function with a parameter
# def welcome(name):
#     print("Welcome to functions in python Mr.\\Ms",name)

# username/name=input('Enter your name: \t')
# #function call
# welcome(username/name)

# function with parameter and return
#kalau nak tambah
# def add(num1,num2):
#     return num1+num2

# fnum=int(input("Enter first number: \t"))
# snum=int(input("Enter Second Number: \t"))
# print(f'Result after adding {fnum} and {snum} is =\t', add(fnum,snum))

#kalau nak multiply (darab)
def multi(num1,num2):
    return num1*num2

fnum=int(input("Enter first number: \t"))
snum=int(input("Enter Second Number: \t"))
print(f'Result after multiplying {fnum} and {snum} is =\t', multi(fnum,snum))