# # Polymorphism=operator overloading
# When the same operator is allowed to have a different meaning according to the context

# operator & Dunder functions:
# a+b         #addition           a.__add__(b)
# a-b         #subtraction        a.__sub__(b)
# a*b         #mul                a.__mul__(b)
# a/b         #div                a.__truediv__(b)
# a%b         #remainder          a.__mod__(b)

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def printcomplex(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self,num2):
        realnew=self.real+num2.real
        imgnew=self.img+num2.img
        return Complex(realnew,imgnew)
     
    def __sub__(self,num2):
        realnew=self.real-num2.real
        imgnew=self.img-num2.img
        return Complex(realnew,imgnew)

num1=Complex(5,6)
num1.printcomplex()

num2=Complex(2,3)
num2.printcomplex()

num3=num1+num2
num3.printcomplex()

num3=num1-num2
num3.printcomplex()

# Output
# 5 i+ 6 j
# 2 i+ 3 j
# 7 i+ 9 j
# 3 i+ 3 j