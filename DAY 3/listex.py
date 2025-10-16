# print('Welcome to List Example')

# my_list = [10,20,30, "Python"] #data yang berbeza

# for item in my_list:
#     print(item)

# my_list = [10,20,30, "Python", None, True, 12,13,46, "Amirah"] #list data yang berbeza
# print('Number of items in list are:',len(my_list))

# for item in my_list:
#      print(item)

#Line menegak
# print("Second Example of list")
# emps=["Sara","Wani","Vi","Sang"]
# print("Number of Employees",len(emps))
# print("All Employees")
# for emp in emps:
#      print(emp)

#Example line melintang
# print("Second Example of list")
# emps=["Sara","Wani","Vi","Sang"]
# print("Number of Employees",len(emps))
# print("All Employees")
# print(emps)

#Example line melintang tanpa ""

# print("Second Example of list")
# emps=["Sara","Wani","Vi","Gara","Alia","Farah"]
# print("Number of Employees",len(emps))
# print("All Employees")
# for emp in emps:
#      print(emp,end=" ")

#Sort Example Accending Order

# emps.sort()
# print('\n Employees in Ascending Order')
# for e in emps:
#      print(e,end=" ")

#reverse example
#listname.reverse()

# emps.reverse()
# print('\nEmployees in Descending Order')
# for e in emps:
#      print(e,end=" ")

#Contoh Descending Order
# print("Second Example of list")
# emps=["Sara","Wani","Vi","Gara","Alia","Farah"]
# print("Number of Employees",len(emps))
# print("All Employees")
# for emp in emps:
#      print(emp,end=" ")

# emps.sort()
# print('\n Employees in Ascending Order')
# for e in emps:
#      print(e,end=" ")

# emps.reverse()
# print('\nEmployees in Descending Order')
# for e in emps:
#      print(e,end=" ")

#Append, remove,pop insert method
# emps=["Sara","Wani","Vi","Gara","Alia","Farah","Betty","Zakwan"]
# print("Number of Employees",len(emps))
# for emp in emps:
#      print(emp,end=" ")

     #append: adds the item at the end of the list
# newEmp=input("\nEnter employee name to add in list: \t")
# emps.append(newEmp)
# print('\nAfter adding New Employee: Number of Employees are:',len(emps))
# for emp in emps:
#      print(emp,end=" ")

#insert(index,item): this will add item at given index
# newEmp=input("\nEnter employee name to add in list: \t")
# pos=int(input("Enter position where you want to insert inside list:\t")) #pos:position
# emps.insert(pos,newEmp)
# print('\nAfter adding New Employee: Number of Employees are:',len(emps))
# for emp in emps:
#      print(emp,end=" ")

# emps=["Sara","Wani","Vi","Gara","Alia","Farah","Betty","Zakwan"]
# print("Number of Employees",len(emps))
# for emp in emps:
#      print(emp,end=" ")
# #list name to remove (item): Will remove item from the list.
# delEmp=input('Employee to remove from the list:\t') #del:delete
# emps.remove(delEmp)
# print(f"Number of Employees after deleting {delEmp} in list are:",len(emps))
# for emp in emps:
#      print(emp,end=" ")

#Cara delete item yang tiada dalam list
# emps=["Sara","Wani","Vi","Gara","Alia","Farah","Betty","Zakwan"]
# print("Number of Employees",len(emps))
# for emp in emps:
#      print(emp,end=" ")

# #list name to remove (item): Will remove item from the list.
# delEmp=input('Employee to remove from the list:\t') #del:delete
# if delEmp in emps:
#      emps.remove(delEmp)
#      print(f"Number of Employees after deleting {delEmp} in list are:",len(emps))
#      for emp in emps:
#           print(emp,end=" ")
# else:
#      print(f'No such item {delEmp} in employee list')

#pop example
#listname.pop(index): will delete element at given index and return its value
# emps=["Sara","Wani","Vi","Gara","Alia","Farah","Betty","Zakwan"]
# print("Number of Employees",len(emps))
# for emp in emps:
#      print(emp,end=" ")

# del_index=int(input('\nEnter index to pop item:\t'))
# print('Pop result: ',emps.pop(del_index))

# print("Number of employees after pop() are:",len(emps))
# for emp in emps:
#      print(emp,end=" ")

#find out first and last element from the list
emps=["Sara","Wani","Vi","Gara","Alia","Farah","Betty","Zakwan"]
print("Number of Employees",len(emps))
for emp in emps:
     print(emp,end=" ")

count=len(emps) #and [-1] #for last element 
print("\n First Element of employees list is: ",emps[0])
print('\n Last Element of employees list is: ',emps[-1])
print('\n Second Last Element of employees list is: ',emps[-2])
print('\n Last Element of employees list is: ',emps[count-1])