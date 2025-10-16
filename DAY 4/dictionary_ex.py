# #Dictionary
# employee= {"id":1,
#         "name":"Sam",
#         "salary":45000.50
#          }

# print("Employees Details as follows:")
# for key,value in employee.items():
#     print(key, "->", value)

# #Adding key in dictionary
# employee["city"]="Selangor" #kalau nak tambah 'city' selepas tulis dictionary di atas
# print('\nDictionary after adding City\n')

# for key,value in employee.items():
#     print(key, "->", value)

# #delete key from dictionary
# del employee["salary"]
# print('\n Employee Details after deleting salary \n')
# for key, value in employee.items():
#     print(key, "->", value)

#key sahaja (id,name, salary) value(1,Sam, 45000.5)
employee= {"id":1,
        "name":"Sam",
        "salary":45000.50
         }
print('All keys from employee ')
for k in employee.keys():
    print(k,end=" ")

#value sahaja
print('\n All values from employee \n')
for v in employee.values():
    print(v,end=' ')

print('\nKey:Value')
for k,v in employee.items():
    print(k," :",v)

print('\nDictionary as follows')
print(employee)