list1=[4,2,3,5]

list1.append(1)    #add one element at end
print("Append=",list1)
list1.sort()       #sort in ascending order
print("sort=",list1)
list1.sort(reverse=True)    #sort in decending order
print("reverse sort=",list1)
list1.reverse()     #just reverse the string
print("Reverse=",list1)
list1.insert(10,100)    #listName.insert(index,element) i.e adding element at specified index
print("After adding elrment at specified index=",list1)

student=["Sonal","Arjun","Vedant"]
student.sort()
print(student)
student.append("Sonal")
print(student)
student.remove("Sonal") #remove 1st occurence of element
print(student)
student.pop(2)  #Remove element at index
print(student)