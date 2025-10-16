# print("We are going to discuss Tuple here")
# subjects=('python','java','dotnet','sql','power bi')
# print('\n All subjects are: \n')
# for sub in subjects:
#     print(sub,end="\t")

# numbers=(1,2,3,4,5,10,2,3,4,4,5,1) 
# print('Total number in tuple:',len(numbers))
# for num in numbers: #display untuk customer
#     print(num,end="\t")

#tupleName.index(item) wil return the index of first occurance of item in tupleName
# numbers=(1,2,3,4,5,10,2,3,4,4,5,1) 
# print('Total number in tuple:',len(numbers))
# for num in numbers: #display untuk customer
#     print(num,end="\t")
# search_num=int(input('\n Enter Number to find out index: '))
# if search_num in numbers:
#     print(f'Index of {search_num} is: \t', numbers.index(search_num))
# else:
#     print(f'No such number {search_num} in our tuple')

#tupleName.count(item): tupleName.count (item) will return number of times item occurs in tupleName
#fungs untuk cari berapa kali number dalam tuple diulang
numbers=(1,2,3,4,5,10,2,3,4,4,5,1) 
print('Total number in tuple:',len(numbers))

for num in numbers: #display untuk customer
    print(num,end="\t")
search_num=int(input('\n Enter Number to find out frequency: '))
if search_num in numbers:
    print(f'Number: {search_num} frequency is: {numbers.count(search_num)} times')
else:
    print(f'No such number {search_num} in our tuple')
    