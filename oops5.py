# example of multilevel inheritance

class Car:
    color="white"

    def start(self):
        print("Car started...")
    
    def stop(self):
        print("car stopped")

class Toyotacar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
    

car1=Fortuner("Disel")
print(car1.type)
car1.start()
print(car1.color)

# Disel
# Car started...
# white


# Multiple inheritance=derived class from multiple base class 

class A:
    varA="Welcome to class A"

class B:
   varB="Welcome to class B"

class C(A,B):
   varC="Welcome to class C"

c1=C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

# Welcome to class C
# Welcome to class A
# Welcome to class B


# super():super() is used to access the static method of the parent class

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()
    

car1=ToyotaCar("Fortunar","Disel")
print(car1.type)
car1.start()
car1.stop()

# Disel
# Car started...
# Car stopped...