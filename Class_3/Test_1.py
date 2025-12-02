class persion:
    def __init__(self,name,age,dob):       #Defining method
        self.name=name                     #attribute
        self.age=age
        self.dob=dob
        self.relative=[]
        self.email=f'{name}@gmail.com'
        x=5                                #Local variable


    def increaseAge(self,n):
        self.age+=n


    def namePrint(self):
        print(f"Name : {self.name}")


    def printEmail(self):
        print(f"Email : {self.email}")


    def addRelative(self,rName):
        self.relative.append(rName)

    def printRelatives(self):
        for i in self.relative:
            print(self.relative)


p1=persion('Hasnat',22,1/1/2001)    #creating object
print(p1.age)
p1.increaseAge(5)
print(p1.age)
p1.namePrint()
p1.addRelative('nafij')
p1.printRelatives()
p1.addRelative('Tesla')
p1.printRelatives()
p1.printEmail()