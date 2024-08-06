# make a class circle with radius 
# calculate Area and perimeter of the function 

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def areaCircle(self):
        return (22/7)*self.radius*self.radius
    
    def perimeter(self):
        return 2*(22/7)*self.radius
    

c1=Circle(21)
print(c1.radius)
print(c1.areaCircle())
print(c1.perimeter())

# 21
# 1386.0
# 132.0

# Add class enginner which inherit the property of employee class 
# add name age to engineer class 

class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetail(self):
        print("Role=",self.role)
        print("Department=",self.department)
        print("Salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Developer","IT",80000)

    def showDetail2(self):
        print("Name=",self.name)
        print("Age=",self.age)        
    

    
# e1=Employee("Software Engineer","IT","70000")
# e1.showDetail()
e2=Engineer("Sonal",28)
e2.showDetail2()
e2.showDetail()

# Role= Software Engineer
# Department= IT
# Salary= 70000

# Another Output
# Name= Sonal
# Age= 28
# Role= Developer
# Department= IT
# Salary= 80000


class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,order2):
        return self.price>order2.price

order1=Order("Book",100)
order2=Order("Notebook",50)

print(order1>order2)        #True
