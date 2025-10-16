import os
# filepath= 'C:\\Users\\mirah\\Desktop\\AIML\\DAY 8\\ourfiles'
filepath= os.getcwd()

filename=input('Enter file name to update file: \t')
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)): #check if the file exist: use if/else
    file=open(fullpath,'a')
    content=input('Enter text to add in file: ')
    file.write(content)
    print(f'File {filename} updated')
    file.close
else:
    print(f'No such file {filename} exists')
