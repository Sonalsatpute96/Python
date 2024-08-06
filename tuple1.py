#string and tuple are immutable
#list are mutable
tup1=()
print(type(tup1))
tup2=(1)    #it will consider as the int datatypeso ','is compulsory
print(type(tup2))
tup3=(1,)
print(type(tup3))
print(tup3)
tup4=(2,3,1,1,1,4)
print(tup4)

#slicing in tuple
print(tup4[1:4])
print(tup4[2: ])
print(tup4[1: ])

#tuple methods
print("Index=",tup4.index(4))    #It will find the element 4 at which index
print("Count of perticular element=",tup4.count(1))