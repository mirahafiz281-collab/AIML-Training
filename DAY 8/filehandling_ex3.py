import os
# filepath= 'C:\\Users\\mirah\\Desktop\\AIML\\DAY 8\\ourfiles'
filepath= os.getcwd()

filename=input('Enter file name to read file: \t')
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)): #check if the file exist: use if/else
    file=open(fullpath,'r')
    content=file.read()
    print(f'File Content as follows')
    print(content)
    file.close()
else:
    print(f'No such file {filename} exists')