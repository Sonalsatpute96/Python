# del=to delete the perticular object or perticular attribute 
class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Sonal")
print(s1.name)      #Sonal
del s1
# print(s1.name)      #NameError: name 's1' is not defined

# Private(like)attribute & method=
# Conceptual impleentation in python
# private attributes and methods are meant to be used only within the class and are not accessible from outside of class 

class Account:
    def __init__(self,acc_no,acc_password):
        self.acc_no=acc_no
        self.__acc_password=acc_password
    
    def reset_password(self):
        print(self.__acc_password)

acc1=Account(12345,5555)
print(acc1.acc_no)
#print(acc1.__acc_password)      #AttributeError: 'Account' object has no attribute '__acc_password'
print(acc1.reset_password())

class Class2:
    def __hello(self):
        print("Hello")

    def welcome(self):
        self.__hello()

c=Class2()
c.welcome()             #Output is Hello as hello fun is private we access withthe help of public function
