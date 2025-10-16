# class Account:
#     def __init__(self,ac_holder,bal):
#         self.ac_holder=ac_holder
#         self.bal=bal

#     def deposit(self, amount):
#         self.bal+=amount
#         print('Balance after deposit',self.bal)

#     def withdraw(self,amount):
#         if(self.bal>=amount):
#             self.bal-=amount
#             print('Balance after withdraw: ',self.bal)
#         else:
#             print('Insufficient amount in account')
#             print('Transaction Failed!!!')
#     def show(self):
#         print(f'Account holder name: {self.ac_holder} Account Balance: {self.bal}')

# # ac1=Account('Sameer',50000)
# # ac2=Account('Chang' ,14000)
# # #To display in output use this:
# # ac1.show()
# # ac2.show()

# #Example 2
# ac1=Account('Sameer', 50000)
# ac1.show()
# #Display untuk kita letak amount yang kita nak
# wamount=float(input('Enter amount to withdraw'))
# ac1.withdraw(wamount)

# class Account:
#     def __init__(self,ac_holder,bal):
#         self.ac_holder=ac_holder

#TASK 2
class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self, amount):
        self.bal+=amount
        print('Balance after deposit',self.bal)

    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('Balance after withdraw: ',self.bal)
        else:
            print('Insufficient amount in account')
            print('Transaction Failed!!!')
    def show(self):
        print(f'Account holder name: {self.ac_holder} Account Balance: {self.bal}')

ac= Account ('Sam', 15000)
ac.show()
print('Please choose: \n 1.Deposit 2.Withdraw 3.Balance Info')
choice=int(input())

if(choice==1):
    damount=float(input('Enter amount to deposit: '))
    ac.deposit(damount)
elif(choice==2):
    damount=float(input('Enter amount to withdraw: '))
    ac.withdraw(damount)
elif(choice==3):
    ac.show()
else:
    print('Wrong choice!')
