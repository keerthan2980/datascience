#class
se1= ["software engineer","raju",21,"juinor","30000"]
se2= ["software engineer","ravi",24,"senior","30000"]

#class
class Software:
    sits_on="always sits" #local variable in the classs
    def __init__(self,name,age,level,salary):
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
    def code(self):
        print(f"{self.name} is coding ")
kee=Software(name="raju",age=21,level="juinor",salary="30000")
kee1=Software(name="ravi",age=23,level="senior",salary="50000")
print(kee.name,kee.age,kee.level,kee.salary)
kee.code()