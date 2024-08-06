#Example of clever if

age=int(input("Enter your age="))
vote=("No,you cannot vote","Yes,you can vote")[age>18]
print("vote=",vote)

sal=float(input("Enter your salary"))
tax=sal(0.1,0.2)[sal>50000]
print("Tax=",tax)