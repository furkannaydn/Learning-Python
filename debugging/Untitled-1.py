class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def inreaseage(self):
        self.age+=1
        
    def decreaseage(self):
        if self.age>0:
         self.age-=1

    def __str__(self):
        return f"{self.name} is {self.age} years old"


p1=person("John",3)
p1.decreaseage()
p1.decreaseage()
p1.decreaseage()
p1.decreaseage()
print(p1)




class Myclass:
    def __init__(self):
        print("Myclass initialized")


    def printSomething(self):
        print("python"),



Myclass=Myclass()
Myclass.printSomething()