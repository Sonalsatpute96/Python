import random

target=random.randint(10,100)

while True:
    userinput=input("Guess the target or 'Quit'")
    if(userinput=='Quit'):
        break
    userinput=int(userinput)
    if(userinput==target):
        print("Congratulations!! Suceesfully Guess")
    elif(userinput<target):
        print("Your number is too small,Take a bigger Guess...")
    else:
        print("Your number is too big ,Take a smaller Guess...")

print("...Game Over...")
