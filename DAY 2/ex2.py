# num=1
# print('Printing numbers from 1 to 100')
# while(num<=100):
#     print(num,end=" ")
#     num+=1 #mesti tulis part ini kalau tidak nombor ini tidak berakhir

#break example (keluar dari loop (perulangan) walaupun kondisi loop belum selesai)
# num=1
# print('Print number from 1 to 100 before we get the numbers divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         break 
#     print(num,end=" ")
#     num+=1

# continue example
# num=1
# while(num<=100):

#     if(num%11==0):
#         num+=1
#         continue 
#     print(num,end="\t")

#     num+=1

# print("Odd Numbers from 1 to 100")
# num=1
# while(num<=100):

#     if(num%2==0):
#         num+=1
#         continue 
#     print(num,end="\t")

#     num+=1


# num=1
# while(num<=100):

#     if(num%2==0):
#         num+=1
#         continue 
#     print(num,end="\t")

#     num+=1  

# num=1
# while(num<=100):

#     if(num%2==0):
#         num+=1
#         continue 
#     print(num,end="\t")

#     num+=1   

# for i in range(1,100):
#     if(i%5==0): #nombor 1 hingga 99 yang boleh dibahagi dengan 5 tidak akan dicetak dan terus sambung nombor seterusnya.
#         continue
#     print(i,end="\t")

# correctPwd='sam123'

# while True:
#  pwd=input('Enter Password to Start the Game: ')
#  if(correctPwd==pwd):
#     print('Welcome to Mobile Legend!!!')

#     break #kita nak pengguna cuba banyak kali sampai berjaya
#  else:
#   print("Wrong Password, try again!!!")
# print ('***Game Started***')

#Contoh Percubaan password 3 kali sahaja
correctPwd='sam123'
counter=0 #password betul hanya ada 1

while True:
 pwd=input('Enter Password to Start the Game: ')
 if(correctPwd==pwd):
    print('Welcome to Mobile Legend!!!')
    print ('***Game Started***')

    break #kita nak pengguna cuba banyak 3 kali sahaja
 else:
  print('Wrong Password!!!')
  counter+=1
  if(counter>=3): #kita nak pengguna cuba banyak 3 kali sahaja
    print('Blocked for 24 hours')
    break #mesti tulis supaya pengguna terus tidak boleh type password
