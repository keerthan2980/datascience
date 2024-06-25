#Class with Inheritance
class Animal:
    def __init__(self,name ):
        self.name=name
class Dog(Animal):
    def speak(self):
        return f" {self.name} will say hello "
class Cat(Animal):
    def speak(self):
        return f" {self.name} will where are yoy"

dog=Dog("jack")
cat=Cat("jack2")
print(dog.speak())
print(cat.speak())