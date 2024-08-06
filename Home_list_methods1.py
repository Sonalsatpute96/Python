# list1=[]
# # list1[0]="Brinjal"
# # print(list1)    #IndexError: list assignment index out of range

# list1.index(0,"Brinjal")
# print(list1)        #TypeError: slice indices must be integers or have an __index__ method

#1.insert():
list1=["Sonal","Swapnil","Sonal"]
list1.insert(1,"Arjun")
print(list1)

#2.index():Need to pass element and it will return index of that element
print(list1.index("Sonal")) #0=as "sonal is present at 0th index"

#3.copy()
list2=list1.copy()
print("**********list2********",list2)
print(list1.copy())     #['Sonal', 'Arjun', 'Swapnil']

#4.append()
list1.append("Bendhale")    #['Sonal', 'Arjun', 'Swapnil', 'Sonal', 'Bendhale']
print(list1)

#5.count()
print(list1.count("Sonal")) #Gives the count of the "Sonal element"

#6.pop()
list1.pop(4)    #give the index it will pop the element
print(list1)    #['Sonal', 'Arjun', 'Swapnil', 'Sonal']

#7.reverse()
list1.reverse()     #reverse the list
print(list1)       #['Sonal', 'Swapnil', 'Arjun', 'Sonal']

#8.sort()
list1.sort()        #sort() the list   
print(list1)        #['Arjun', 'Sonal', 'Sonal', 'Swapnil']

#9.remove()
list1.remove("Sonal")
print(list1)        #remove 1st occurence of sonal

#10.#extend>> used to append elements from another iterable
#Extend merge 2
family_list=["Sanjay","Jayshri","saurabh","Suman_ajji","sakharam ajoba"]
list1.extend(family_list)
print("Extend",list1) #Extend ['Arjun', 'Sonal', 'Swapnil', 'Sanjay', 'Jayshri',
#'saurabh', 'Suman_ajji', 'sakharam ajoba']

#11.clear()=clear all elements
family_list.clear()
print(family_list)      #[]
print(type(family_list))


list2=["Sonal"]
list3=["Arjun","Swapnil"]
print(list2+list3)      #['Sonal', 'Arjun', 'Swapnil']
print(list3+list2)      #['Arjun', 'Swapnil', 'Sonal']

#repeatation operation
print("*"*5)        #*****
print("_"*50)       #__________________________________________________
print("0"*10)       #0000000000
print([0]*10)       #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print([1, 2, 3] * 10)#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(list(range(1, 6)) * 3)    #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
msg="Your appointment will be tommorow \n"
print(msg*3)        #Your appointment will be tommorow Your appointment will be tommorow Your appointment will be tommorow

# membership in , not in
grocery_list = ["Milk", "Orange", 1, 2, 3, True, 2+4j, 2.3]
print("milk" in grocery_list)   #False
print("Milk" in grocery_list)   #True
print("Banana" not in grocery_list) #True

print("grocery_list=",grocery_list)

#shallow copy>> value will change with change in other list|
b=grocery_list
print("Shallow copy b=",b)

grocery_list[0]="Banana"        #updation in grocery_list will applied on b(Shallow copy)
print("grocery_list",grocery_list)  #grocery_list ['Banana', 'Orange', 1, 2, 3, True, (2+4j), 2.3]
print("b=",b)                 #b= ['Banana', 'Orange', 1, 2, 3, True, (2+4j), 2.3]

#deep copy will not change with change in other list
a=grocery_list.copy()
grocery_list[2]="Mango"
print("grocery_list",grocery_list)  #grocery_list ['Banana', 'Orange', 'Mango', 2, 3, True, (2+4j), 2.3]
print("deep copy a=",a)             #a= ['Banana', 'Orange', 1, 2, 3, True, (2+4j), 2.3]

grocery_list[0] = "Guava"
print("grocery_list",grocery_list)  #grocery_list ['Guava', 'Orange', 'Mango', 2, 3, True, (2+4j), 2.3]
print("b=",b)                       #b= ['Guava', 'Orange', 'Mango', 2, 3, True, (2+4j), 2.3]

#sorting lists

book_list = ["Data Structure", "Algorithm", "Web dev"]
print(sorted(book_list))
book_list
print(book_list.index("Algorithm"))
print(book_list.index("Web dev"))
book_list = ['Data Structure',"Data Structure", 'Algorithm', 'Web dev']
print(book_list)
print(book_list.count('Data Structure'))
book_list.remove('Data Structure')
print(book_list)
del book_list
#print(book_list)       #NameError: name 'book_list' is not defined
