#Filter (tapis nombor yang kita nak sahaja)
# numbers = [10,25,30,40,2,1]

# print('Original List\n')
# for num in numbers:
#     print(num,end=" ")

# even_numbers= list(filter(lambda x: x%2==0, numbers))

# print('\nEven Numbers from list as follows\n')
# for num in even_numbers:
#     print(num, end=" ")

#Task 2
#You have following list
#write code using filter to find out all the number less than 5 from the list

# our_list=[4,2,5,6,7,3,1,10]
# print('Original List\n')
# for num in our_list:
#     print(num,end=" ")

# our_numbers= list(filter(lambda x: x<5, our_list))

# print('\nNumbers less than 5 from list as follows\n')
# for num in our_numbers:
#     print(num,end=" ")

#Filter Example in dictionary
#Student dictionary
students_marks={'Sam':60,
                'Raj':55,
                'Mia':32,
                'Gia':89,
                'Wina':40,
                'Jaja':23,
                }
print('All Student')
print(students_marks) 
for k,v in students_marks.items():
    print(f'Name: {k} -> Marks {v}')

pass_students=dict(filter(lambda i:i[1]>=50, students_marks.items()))
print('Passed Student')
print(pass_students)
for k,v in pass_students.items():
    print(f'Name: {k} -> {v}')

#Sorting key #key(names)=0 #value(marks)=1
sort_pass_students=dict(sorted(pass_students.items(), key=lambda x: x[1])) #0=Names #1=Marks
print('Ascending Order')
for k,v in sort_pass_students.items():
    print(f'Name: {k} -> Marks {v}')

sort_pass_students_desc=dict(sorted(pass_students.items(), key=lambda x: x[1], reverse=True))
print('Descending Order')
for k,v in sort_pass_students_desc.items():
    print(f'Name: {k} -> Marks {v}')




