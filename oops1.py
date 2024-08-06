# To map with real world scenario we started to use object oriented programming
# class is blueprint to create object

class Student:
    name="Sonal"

s1=Student()
print(s1.name)
s2=Student()
print(s2.name)

class Car:
    color="Red"
    brand="Mercedes"

c1=Car()        #() is used to call the constructor
print(c1.color)
print(c1.brand)

# Sonal
# Sonal
# Red
# Mercedes

# __init__ function=All class have a function called __init__()
# which always executed when class is being initialized

# creating a class                                    Creating object
# class student:                                      s1=Student("karan")
#     def __init__(self,fullname):                    print(s1.name)
#         self.name=fullname
#self means itself....so it point to object created by the class

# The self parameter is the reference to the current instance of the class and used to access variable that belongs to that class 

class Stu:
    # default constructor it automatically creted by python
    # def __init__():
    #     pass

    #parameterized constructor
    # here try to give same name as name and fullname let me give eg of marks
    college_name="Dr.D.Y Patil Instutute of pune"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print(self)

s1=Stu("Sonal",90)
print(s1.name,s1.marks)
print(s1)
s2=Stu("Swapnil",94)
print(s2.name,s2.marks)
print(s2)
print(Stu.college_name)

# so the location of self and the object is same i.e self point to object 
# <__main__.stu object at 0x0000025EF86D67B0>
# Sonal 90
# <__main__.stu object at 0x0000025EF86D67B0>
# <__main__.stu object at 0x0000025EF86D6660>
# Swapnil 94
# <__main__.stu object at 0x0000025EF86D6660>

#eg of claas attribute =college_name        to print Class_name.attribute
# eg of oject attribute in above eg is name,marks etc               To print object_name.attribute

class Book:
    Standard="First Year"
    def __init__(self,name,publication):
        self.name=name
        self.publication=publication
    
    def welcome(self):
        print("Welcome to first year syllabus",b1.name)
    
    def get_publication(self):
        return b2.publication


b1=Book("C Programming","ABC")
print(b1.name,b1.publication)
b1.welcome()

b2=Book("DSA","XYZ")
print(b2.name,b2.publication)
print(b2.get_publication())

# C Programming ABC
# Welcome to first year syllabus C Programming
# DSA XYZ
# XYZ

# QUE-Create a class which store the name and marks of 3 student and make fun for average of all 

class Class1:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("Hello")
    def average(self):
        sum=0
        for val in self.marks:
            sum=sum+val
        print("Name=",self.name,"average=",sum/3)


s1=Class1("Sonal",[90,89,91])
s2=Class1("Swapnil",[93,94,95])
s3=Class1("Arjun",[99,100,98])
print("Marks of the 3 student:")
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s3.name,s3.marks)

print(s1.average())
print(s2.average())
print(s3.average())

Class1.hello()          #static method

# Marks of the 3 student:
# Sonal [90, 89, 91]
# Swapnil [93, 94, 95]
# Arjun [99, 100, 98]
# Name= Sonal average= 90.0
# None
# Name= Swapnil average= 94.0
# None
# Name= Arjun average= 99.0
# None
#Hello

# Static method 
# method that don't use the self parameter (Work at a class level)
# class student:
#     @staticmethod       #decorator
#     def college():
#         print("Dr.D.Y Patil college")

# decorator=allow us to wrap another function in order to extend the behaviour of wrapped function,without
# permantly modify it