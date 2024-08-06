#what is operator>>> special keywords to perform operations
#why? To manipualte data

#arithmatic operator

a=5
b=5
print("Additiom",a+b)

add=5+10
print("Add=",add)
print("Sub=",5-2)
print("mult=",5*5)
print("Div=",10/2)  #return float value as 5.0
print("Modulus",10%2)
print("Modulus",10%3)
print(2**2) #2^2
print(2**3) #2^3
print(4/3)
print("Floor Operator=",4//3)   #it convert float to nearest int

a=2
print(a)

# Comparison operator >> compare two values>> return a boolean value
print("2==2",2==2)
print("2!=2",2!=2)
print("5!=2",5!=2)
print("10 < 5",10 < 5)
print("10>5",10>5)
print("10 >= 10",10>=10)
print("10>=1",10>=1)
print("10<=12",10<=12)

#Logical operator
#and
print("and operator")
print(True and True)
print(True and False)
print(False and False)

#or
print("or operator")
print(False or False)
print(True or False)
print(True or True)

#Not operator
print("not operator")
print(not True)
print(not False)

#Assignment operator
print("Assignment operator")
a=5
print(a)
a=a+10
print(a)
a+=10
print(a)
a*=2
print(a)
a/=10
print(a)

#membership operator
print("#membership operator")

s="Sonal"
print("P" in s) #false
print("S" in s) #True
print(s)

print("Arjun" in "Arjun is my 3 year old baby") #true
print("arjun" in "Arjun is my 3 year old baby") #false
print("arjun" not in "Arjun is my 3 year old baby") #true
print("Data" in "Datastucture") #True

list1=["Sonal","Arjun","Swapnil"]
print("Swapnil" in list1)   #True

#identity operator >> compare the memory location of two object
print("Identity operator >> compare the memory location of two object")
A=5
B=5
print(A is B)       #True
C=9
print(C is A)       #False
print(C is not A)   #True

s1 = "Sonal Bendhale"
b=s1
print(s1 is b)      #True
print(b is s1)      #True

str1="Sonal"
str2="Bendhale"
print(str1 is str2)         #false
print(str1 is not str2)     #True

#bitwise operator>> operations at bit level
print("Bitwise operator>> operations at bit level")
print(10 & 10)
print(10 & 3)
bin(10)
bin(18)
bin(3)
bin(2)

print("bitwise or")
print(3 | 5)
bin(3)
bin(5)

#negation
print("negation")
print(~3)
~100
~6

print("#Bitwise xor >> return 1 when exactly one operand is 1")

5 ^ 3
bin(5)
bin(3)
bin(6)


print("#shift >> left shift and right shift")
print("#left shift put no of zeros on right side")

print(35 << 3)
bin(35)
bin(280)
5 << 1
bin(5)
bin(10)

print("#Right shift operator >> remove the no of elements in the binary")
print(280 >> 3)
bin(280)
bin(35)
print(10 >> 1)
bin(10)
bin(5)

print("## order of precedence")
#execution will start from left
print(2+3-1)

print("#always parenthesis")

print((5+3) - 4)
print(4 - (5+3))
print((10+5) + (8/2))


