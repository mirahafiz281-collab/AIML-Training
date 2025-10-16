# #All classes
# import datetime
# import inspect

# print('Today is (Date):',datetime.date.today())

# dtclasses = inspect.getmembers(datetime, inspect.isclass)
# print('All Classes inside datetime module')

# for n, func in dtclasses:
#     print(n)

# print('All functions inside datetime.date class')

# functions = inspect.getmembers(datetime.date, inspect.isbuiltin)
# for n, func in functions:
#     print(n)

import os

dirs=os.listdir() #dir= directly
for dir in dirs:
    print(dir)