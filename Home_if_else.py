course="Python Developer"
if(course=="Python Developer"):
    print("I am a python developer")

marks=int(input("Enter marks="))    #need to mention int
if(marks>90):
    print("A+ Grade")
else:
    print("B Grade")

number=42
if(number%2==0):
    print("Number is even")

temp=float(input("Enter temp"))
if(temp>25):
    print("Its warm")

age=18
if(age>18):
    print("Adult")
else:
    print("Not adult")

score=70
passing_score=75
if(score<=passing_score):
    print("You are almost pass ")
else:
    if(score<=passing_score-5):
        print("You are pass")
    else:
        print("You are fail")


