# class Player:
#     def __init__(self):
#         print('Welcome to Player Class')
    
#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self):
#         print(f'Id:{self.id} \t Name: {self.name} \t Team: {self.team} ')


# #Object creation
# p1=Player()
# p2=Player()
# p3=Player()
# p1.reg(1,'MSD','India')
# p2.reg(2, 'R.Khan', 'Afghanistan')
# p3.reg(3, 'Ali', 'England')

##Displaying the details
# p1.display()
# p2.display()
# p3.display()


#PARAMETER CONSTRUCTOR
class Player:
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f'Id:{self.id} \t Name: {self.name} \t Team: {self.team} ')

    def __str__(self):
        return f'{self.id} {self.name} {self.team}' #tambah ini utk guna yang print(p1) and so on


#object creation

p1=Player(1,'MSD','India')
p2=Player(2, 'R.Khan', 'Afghanistan')
p3=Player(3, 'Ali', 'England')

#Displaying first player details
# p1.display()
# p2.display()
# p3.display()

#how to directly type the display (calling the object) tambah code return di atas
print(p1)
print(p2)
print(p3)
