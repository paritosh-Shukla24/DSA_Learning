# class Student:
#     def __init__(self,name):
#         self.name1=name

#     def getname(self):
#         return self.name1
    
#     def setname(self,name):
#         self.name1=name


# s=Student("Bob")
# print(s.getname())
# s.setname("Paritosh")
# print(s.getname())

# class Animal:
#     def sound(self):
#         print("Animal make sound")

# class Dog(Animal):
#     def bark(self):
#         print("Baww Baww")

    
#     def sound(self):
#         print("Baww Baww")

# dog=Dog()
# dog.sound()
# dog.bark()


# class Add:
#     def sum(self,a,b=0,c=0):
#         return print(a+b+c)
    

# calc=Add()

# calc.sum(5)
# calc.sum(5,19)
# calc.sum(5,10,50)

##Abstraction

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Sttarted..........")


c=Car()
c.start()