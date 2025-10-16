#print("Write a function to findout the cube of given number")
#5 : 5*5*5 (e.g. cube of 5 is 5*5*5 means 125)

##Task 1
# def cube(num):
#     return num*num*num
# given_num=int(input('Enter Number to find out cube of number:\t'))
# print(f'Number is: {given_num} cube is',cube(given_num))

#Task 2
#write a function to calculate bonus of given salary
#function take salary as input and return bonus 10% of salary.

def calc_bonus(salary):
    return salary*0.10

salary=float(input("Enter your salary to find out your bonus: "))
print(f"Salary is: {salary} bonus is:",calc_bonus(salary))