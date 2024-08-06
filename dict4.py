Subject_dict={}

x=int(input("Enter a marks of phy"))
y=int(input("Enter the marks of chem"))
z=int(input("Enter the marks of maths"))

Subject_dict.update({"phy=":x})
Subject_dict.update({"chem=":y})
Subject_dict.update({"Math=":z})

print("Final dictionary=",Subject_dict)