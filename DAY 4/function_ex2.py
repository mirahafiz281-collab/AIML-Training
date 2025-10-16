#default parameter in functions
# def info(id,name,city='KL'):
#     print(f"Details as follows \n ID: {id} Name: {name} City: {city}")

# info(1,'Sam','New Delhi')
# info(102,"Xi")
# info(3,'Chang')

#we want to create a single method that can abble to add 2 numbers, 3 numbers,4 numbers, or numbers
#and return correct total

#Default
 #tambah value, jika tiada value=0 (default)
 #n1=1 n2=2 n3=0,n4=0,n5=0
 #n1=4 n2=6 n3=2 n4=10 n5=2
 #n1=5 n2=25 n3=10 n4=0 n5=0

# def add(n1,n2,n3,n4,n5):
#     return n1+n2+n3+n4+n5
# print("Result: ",add(1,2,3,7,0)) 
# print("Result: ",add(4,6,2,10,2)) 
# print("Result: ",add(5,25,10,0,0)) 

# def add (*nums):
#     return sum(nums)
# print('Sum of 1,2,3,11,12 is \t',add(1,10,11))
# print('Sum of 5,2 is \t',add(5,2))
# print('Sum of 10,20,30,11,120 is \t',add(10,20,30,11,120))

# print('Maximum Example')
# print('Maximum of 1,10,11 is: \t',max(1,10,11))
# print('Maximum of 5,2 is \t',max(5,2))
# print('Maximum of 10,20,30,11,120 is \t',max(10,20,30,11,120))

# print('Minimum Example')
# print('Minimum of 1,10,11 is: \t',min(1,10,11))
# print('Minimum of 5,2 is \t',min(5,2))
# print('Minimum of 10,20,30,11,120 is \t',min(10,20,30,11,120))


