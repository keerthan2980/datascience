#Class with Getter and Setter Methods
class Bank:
    def __init__(self,name,accountno,amount=0):
        self.name=name
        self.accountno=accountno
        self.amount=amount
    def deposit(self,deamount):
        if deamount>0:
            self.amount+=deamount
        return f" the new amount is {self.amount} and the debited amount is {deamount}"

    def cerdit(self,other):
        if other > 0 and other<self.amount:
            self.amount -=other
        return f"the new amount is {self.amount} and cerideted amount is {other}"

a=Bank(name="axis",accountno=6222,amount=50)
print(a.name,a.accountno,a.amount)
print(a.deposit(100))
print(a.cerdit(10))

