# class Bird:
#     def fly(self):
#         print('Bird can fly')

# class Airplane(Bird):
#     def fly(self):
#         print('Airplane fly')

# b=Bird()
# print('Bird Implement')
# b.fly()

# print('Airplane Implementation')
# a=Airplane()
# a.fly()

# print('Using for loop')
# for obj in [Bird(), Airplane()]:
#     obj.fly()

#Example 2
class Emp:
    def reg(self):
        self.id=int(input ('Enter Id'))
        self.name=input('Enter Name: ')

    def disp(self):
        print('Name: ', self.name)
        print('ID: ',self.id)

class Dev(Emp):
    def reg(self): 
        super().reg() # call semula 'Name dan Id' di atas tanpa perlu salin semula
        self.domain=input('Enter Domain: ')

    def disp(self):
        super().disp()
        print('Domain: ',self.domain)

d1=Dev() #Dev=Developer
d1.reg()
d1.disp()