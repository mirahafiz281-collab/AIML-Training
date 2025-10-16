#Constructor inheritence
class Emp:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual

    def display(self):
        print('ID: ',self.id)
        print('Name: ',self.name)
        print('Quali: ',self.qual)

class Dev(Emp):
    def __init__(self, id, name, qual, domain, project):
        super().__init__(id, name, qual) #keyword penting
        self.domain=domain
        self.project=project

    def display(self): #display=method name (boleh tukar nama display tu) user function
        super().display()
        print('Domain: ',self.domain)
        print('Project: ',self.project)

#Task 1
#create one Emp object with id=1, name='Sam', qual='MCA'
emp=Emp(1, 'Sam', 'MCA')
#create one Dev object with id=3, name=Ravi, qual='Mtech', project='eshopping', Domain='dot net'
dev=Dev(3,'Ravi', 'Mtech', 'dot net', 'eshopping')

#Untuk maklumat itu keluar dalam output
#Display Dev details
print('Developer Details as follows')
dev.display()

#Display Emp details
print('Employee details as follows')
emp.display()
