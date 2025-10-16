#Cara nak buka fail baru dalam VS Code dan tulis sesuatu dalam fail itu
#cara ambil file_path, bahagian kiri > create new folder (ourfiles) > right click mouse > pilih Copy Path

# import os
# file_path=r'C:\Users\mirah\Desktop\AIML\DAY 8\ourfiles\sample.txt' #Paste dalam ni tambah file baru (\sample.txt)

# #Ini untuk tulis text dalam file sample tu
# file=open(file_path,'w')
# content=input('Enter text to write in file: ')
# file.write(content)
# file.close


# #Minta user masukkan new file name
#3 cara untuk filepath
# 1. filepath=r'C:\Users\mirah\Desktop\AIML\DAY 8\ourfiles' (use r' ')
# # or can use
# 2. filepath= 'C:\\Users\\mirah\\Desktop\\AIML\\DAY 8\\ourfiles' (use double \ without r' ')
#or use
# 3. filepath=os.getcwd (kalau nak create file dalam Day 8)

import os
filepath= 'C:\\Users\\mirah\\Desktop\\AIML\\DAY 8\\ourfiles'
filename=input('Enter file name to create file: \t')
fullpath=os.path.join(filepath,filename)
file=open(fullpath,'w')
content=input('Enter text to write in file: ')
file.write(content)
print(f'File {filename} create at {fullpath} and content saved in file')
file.close()