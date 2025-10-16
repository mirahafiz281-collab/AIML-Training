# import os
# import inspect
# print ('Current directory: ',os.getcwd())

# functions= inspect.getmembers(os,inspect.isbuiltin)

# print('All Function in os module')
# for n,func in functions:
#     print(n)

#For import os
# import os
# print ('Current directory: ',os.getcwd())

#TASK 1
#Create a folder inside current directory using python
#ia create folder baru di dalam python ini
# import os
# cdir=os.getcwd() #current directory
# folder_name=input('Enter Folder Name to create: ')
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder Already Exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')

#Task 2
#Rename a folder
# os.rename(folder_name, renamed_folder)
# write code to rename a folder
# you will take folder name from user 
# if it is exist, you will ask new name and rename it

import os
cdir=os.getcwd() #current directory
your_folder=input('Enter your folder name to rename: ')
new_name=input('Enter new name folder: ')

your_folder_path=os.path.join(cdir,your_folder)
new_name_path=os.path.join(cdir, new_name)

if(os.path.exists(your_folder_path)):
    os.rename(your_folder_path, new_name_path)
    print(f'Folder renamed from {your_folder} = {new_name}')

else:
    print(f'{your_folder} Folder does not exist!')


