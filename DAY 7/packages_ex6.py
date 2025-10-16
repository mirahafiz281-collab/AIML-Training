#Packages in Python (Welcome.py)
#Cara 1
# from ourpack import welcome
# username=input('Please enter your name: ')
# welcome.display(username)

# msg=welcome.display(username)
# print('Message for you: ', msg)

#Packages Student.py
from ourpack import student
s1=student.student(1, 'Ravi')
s1.print_info()