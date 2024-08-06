list1=[1,2.2,3+5j,True,"Sonal"]
print(list1)
print(type(list1))

print(list1[2])
list1[2]=5+5j
print(list1)

#Mutable=Updation is possible
str1="Sonal"
print(str1)

print(str1[2])
#str1[2]="s"        #TypeError: 'str' object does not support item assignment
#immutable=updation is not possible