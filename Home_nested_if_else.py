#Nested 'if-else' Statement

course="Python Developer"
grade=8
if(course=="Python Developer"):
    if(grade>7):
        print("sucessfull")
    else:
        print("failed")
    
marks=78
if(marks>=80):
    if(marks>=90):
        print("A Grade")
    else:
        print("B Grade")
else:
    print("C Grade")

is_weekend=True
is_sunny=True
if is_weekend:
    if is_sunny:
        print("Go for picnic")
    else:
        print("Stay in and relax")
else:
    print("It's working day")

is_student=True
is_teacher=True
if is_student:
    if is_teacher:
        print("You are the student as well as teacher")
    else:
        print("yOU ARE student but not teacher ")
else:
    if is_teacher:
        print("You are teacher not a student")
    else:
        print("nor teacher nor student")

vip=True
age=66

if vip:
    if(age>=18):
        if(age<65):
            print("VIP")
        else:
            print("pricing is not for senior")
    else:
        print("Not for adults")
else:
    print("Regular pricing")

