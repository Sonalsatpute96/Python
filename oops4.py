class Car:
    color="White"
    
    def start(self):
        print("car started...")

    def stop(self):
        print("car stopped...")

class Toyotacar(Car):
    def __init__(self,name):
        self.name=name

car1=Toyotacar("Fortuner")
car2=Toyotacar("prius")

print(car1.name)
car1.start()        #this is the car method still it will work as Car clas is inherited by Toyotacar class
car2.stop()
print(car1.color)

# Fortuner
# car started...
# car stopped...
# White


Types of inheritance
1.single inheritance
2.multi level inheritance
3.multiple inheritance
