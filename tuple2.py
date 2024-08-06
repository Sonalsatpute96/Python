#program to find no of 'A' grade from tuple
tup1=("A","B","C","A","A","D")
my_tuple=list(tup1)
my_tuple.sort()
print("Sorted tuple=",my_tuple)
n=tup1.count("A")
print("No of 'A' grade=",n)
