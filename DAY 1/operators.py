#Assignment operators: =, +=, -=
# price=float(input('Enter Product Price: '))
# discount=price*0.10
# disPrice=price-discount
# print(f'Price: {price} \nDiscount: {discount} \nDiscountedPrice:{disPrice}')

# #Salary and Bonus
# salary=500.00
# bonus=50.00
# print(f'Salary {salary} and Bonus {bonus}')
# salary+=bonus #salary=salary+bonus
# print("Salary with bonus: ",salary)

# #Salary and tax
# salary=500.00
# tds=salary*0.10
# print(f'Salary {salary} and TDS {tds}')
# salary-=tds #salary=salary-tds
# print("Salary after tax: ",salary)

#Comparison operators: ==, >, >=, <, != etc.
#if (condition):
    #letak code
#else:
    #letak code

# #Example 1
# age=int(input("Enter your age: "))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("You are not eligible to cast your vote")

# print("End of Programme")

# #Example 2
# marks=int(input("Enter mark percentage without '%' sign"))
# if(marks,30):
#    print("Fail in exam")
# else:
#    print("Clear the Exam")

# #Example 3
#Your access Code="wes12"
# accessCode=input("Enter Access Code: ")
# if(accessCode!="wes12"):
#     print("Invalid Access Code")
# else:
#     print("Welcome to your course")

# #Example 4
# == means equal
# accessCode=input("Enter Access Code: ")
# if(accessCode=="wes12"):
#     print('Welcome to our couses')
# else:
#     print("Invalid Access Code")

# #Example 5
# #Logical operators: and, or, not
# phyMarks=int(input("Enter marks obtained in Physics: "))
# cheMarks=int(input("Enter marks obtained in Chemistry: "))
# mathMarks=int(input("Enter marks obtained in Mathematics: "))

# if((mathMarks>=50) and (phyMarks>=55) and (cheMarks>60)):
#     print("You are eligible to sit in pre exam of MBBS")
# else:
#     print("You have not got the required marks")

# #Example 6
# idProof=input("Enter Id proof you have: ")
# if((idProof=="passport")or(idProof=="dl")):
#     print(f"valid Id {idProof} we accept here")
# else:
#     print("Only passport,dl and voter id are accepted as Identity Proof")
#     print(f"{idProof}: is not valid ID here")

# #Example 7
# mathMarks=int(input("Enter marks obtained in Mathematics: "))
# gapYear=int(input("Enter Year gap if any otherwise 0 "))
# if((mathMarks<=55) and (gapYear != 0)):
#     print("Not eligible for BTech")
# else:
#     print("Eligible for BTech")

# #Example 8
name=input("Enter username: ")
if(not name):
    print("Error!!!")
else:
    print("Welcome",name)