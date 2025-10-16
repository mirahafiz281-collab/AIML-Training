# print("Sets in Python"): #Set itu unordered (tidak ikut ordered selain list)
# set_one={'laptop','ipad','mobile','headphone','laptop','ipad'}
# print('Number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#clear():remove all the items from set
# set_one={'laptop','ipad','mobile','headphone','laptop','ipad'}

# set_one.clear()
# print('\n After clear number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#remove set
# set_one={'laptop','ipad','mobile','headphone','airphone'}
# print('\n Number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

# #set.remove(item):updates the set and removes item from set.
# set_one.remove('airphone')
# print('\n After removing one item from set:',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#union,intersection, difference


#union : nombor duplicate tidak akan ditunjukkan dalam output
#s1.union(s2):Returns a new set with all items from both sets s1,s2
# print(f'set one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# unionset=set_one.union(set_two,set_three)
# print(f' Union of set_one, set_two and set_three contains: {len(unionset)} following items')

# print(unionset)

#Intersection example (output:nombor yang berulang dari kedua set akan dinyatakan)
#s1.intersection(s2): return set which contains only item in both sets s1,s3...
# set_one={100,200,300,500,150,700,900}
# set_two={100,400,1000,700,1300}
# print(f'set one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# newset=set_one.intersection(set_two)
# print(f'Intersection of set_one, set_two contains: {len(newset)} following items')
# print(newset)

#Difference example
#s1.difference(s2): Return set which contains only item those are in s1 but not in s2.
set_one={100,200,300,500,150,700,900}
set_two={100,400,1000,700,1300}
print(f'set one contains: {len(set_one)} items')
print(set_one)
print(f'set_two contains: {len(set_two)} items')
print(set_two)
newset=set_one.intersection(set_two)
print(f'Difference of set_one, set_two contains: {len(newset)} following items')
print(newset)
