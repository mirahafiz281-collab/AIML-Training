#Exception= kita nak handle output program itu, sekiranya terdapat kesalahan kecil yang jarang berlaku,
#supaya program dapat tulis propper mesej for error programming (kita tak nak out error tu stuck di situ)

# try:
#     num1=float(input('Enter first number: '))
#     num2=float(input('Enter second number: '))
#     total=num1+num2
#     print(f'Sum of {num1} and {num2} = {total}')
# except Exception as e:
#     print('Error ',e)
# finally:
#     print('End of Program')

#Example 2
try:
    num1=float(input('Enter first number: '))
    num2=float(input('Enter second number: '))
    total=num1+num2
    print(f'Sum of {num1} and {num2} = {total}')
except Exception as e:
    print('Error ',e)
finally:
    print('End of Program')