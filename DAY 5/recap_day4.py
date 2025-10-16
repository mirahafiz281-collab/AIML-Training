# #Example 1 functions
# def display():
#     print('Welcome to recap of functions')

# display()

# #Example 2 functions (letak nama)
# def welcome(name):
#     print('Welcome to functions Mr.\\Ms.', name)

# welcome('Amirah')

# #Example 3 (letak nombor Cube)
# def cube(num):
#     cube_num=num*num*num
#     print(f'Cube of given number: {num} is =\t {cube_num}')

# my_num=int(input('Enter number to find out Cube:\t'))
# cube(my_num)

# #Example 4 (semua  di atas)
# def welcome(name):
#     print('Welcome to functions Mr.\\Ms.', name)

# def cube(num):
#     cube_num=num*num*num
#     print(f'Cube of given number: {num} is =\t {cube_num}')

# def square(num):
#     return num*num

# username=input('Enter User Name: \t')
# my_num=int(input('Enter number to find out cube and square: \t'))

# welcome(username)
# cube(my_num)
# sq=square(my_num)
# print(f'Square of {my_num} is {sq}')

#Example 5
# def salBonus(salary):
#     return salary*0.10

# my_sal=float(input('Enter salary to find out Bonus: \t'))
# Bonus=salBonus(my_sal)
# print(f'Salary: {my_sal} Bonus: {Bonus}')
# print(f'Salary after bonus =\t {my_sal+Bonus}')

#Example 6
def salBonus(salary):
    bonus=salary*0.10
    print(f'Salary: {salary} Bonus: {bonus}')

my_sal=float(input('Enter salary to find out Bonus: \t'))
salBonus(my_sal)
