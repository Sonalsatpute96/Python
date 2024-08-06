# Class methods 
# A class method is bound to the class & receives the class as an implicit first arguments

# Note-static method can't acess or modify class state & generally for utility

# class Student:
#     @classmethod    # Decorator
#     def college(cls):
#         pass

# Revision=3 types of methods
# 1.staticmethod =use when no class methods or instance method/attribte is to use 
# 2.class method =use when class method/attribute is to use/access
# 3.instance method(self) =use when instance method/attribute is to use/access

# class Student:
#     name="anonymus"

#     def changename(self,name):
#         self.name=name

# s1=Student()
# s1.changename("Sonal")
# print(s1.name)
# print(Student.name)

# Output
# Sonal
# anonymus

# class Student:
#     name="anonymus"

#     def changename(self,name):
#         self.__class__.name=name

# s1=Student()
# s1.changename("Sonal")
# print(s1.name)
# print(Student.name)

# Output:
# Sonal
# Sonal


class Student:
    name="anonymus"

    @classmethod
    def changename(cls,name):
        cls.name=name

s1=Student()
s1.changename("Sonal")
print(s1.name)
print(Student.name)

# Output:
# Sonal
# Sonal

# Property decorators=Didn't get what is property decorator

class Student1:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    # def percentage(self):
    #     self.per=(self.phy+self.chem+self.math)/3
    #     print(self.per)

    # @property
    def percentage(self):
        self.per=(self.phy+self.chem+self.math)/3
        print(self.per)


s2=Student1(98,97,99)
# s2.percentage()
s2.phy=88
s2.percentage()