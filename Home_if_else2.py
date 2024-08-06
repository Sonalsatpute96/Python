#if-elif-else

course="python Developer"
if(course=="python Developer"):
    print("You selected Python developer course")
elif(course=="Data science"):
    print("you selected datascience course")
else:
    print("You had not enrolled for any course")


Grade=5
if(Grade>=7):
    print("Excellent")
elif(Grade>=5):
    print("Good")
else:
    print("Need to work")

marks=85
if(marks>=90):
    print("Grade A")
elif(marks>=80):
    print("B Grade")
else:
    print("Below B Grade")

num=0
if(num>0):
    print("No is +ve")
elif(num<0):
    print("No is -ve")
else:
    print("Num=0")

age=80
if(age<18):
    print("You are a minor")
elif(18<=age<65):
    print("You are adult")
else:
    print("You are senior citizen")

#if else:

is_raining=True
if is_raining:
    print("Bring umbrella")
else:
    print("Enjoy sunshine")

num=7
if(num%2==0):
    print("Even")
else:
    print("Odd")

#Ternary operature:
score=80
result="Pass" if(score>70) else "Fail"
print("result=",result)