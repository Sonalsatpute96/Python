#List are ordered collection of items
#[]
#list is like a shopping bag which can store everything

list1=[1,2.2,2+3j,"sonal",(1,2,3)]
print(list1)
print(type(list1))

#lists are mutable
print(list1[0]) #1
print(list1[1]) #2.2
print(list1[2]) #(2+3j)
print(list1[-1])    #(1, 2, 3)
print(list1[-2])    #sonal

#Slicing

print(list1[1:3])   #[2.2, (2+3j)]
print(list1[2:])    #[(2+3j), 'sonal', (1, 2, 3)]
print(list1[:3])    #[1, 2.2, (2+3j)]
print(list1[::-1])  # will print reverse list [(1, 2, 3), 'sonal', (2+3j), 2.2, 1]
print(list1[::2])   #[1, (2+3j), (1, 2, 3)]
print(list1[::-2])  #[(1, 2, 3), (2+3j), 1]
print(list1[1:3:1]) #[2.2, (2+3j)]
print(list1[1:3:-1])#[] as start with 1 to 3 but -1 so -ve axis side so null
print(list1[3:1:-1])#['sonal', (2+3j)] start with 3 to 1 and -1 so -ve side

movies = ["Action1", "Action2", "Action3","comedy1"]
print(movies[3])        #comedy1
print(movies[::-1])     #['comedy1', 'Action3', 'Action2', 'Action1']
print(movies[2::-1])    #['Action3', 'Action2', 'Action1']*********************REMEMBER

pages = ["Title page", "chap1", "chap2", "conclusion", "index"]
print(pages[-1])
pages[1]="CHAP_1"   # updation is possible
print(pages)        #['Title page', 'CHAP_1', 'chap2', 'conclusion', 'index']

queue = ["Ajay", "Bijay", "Sanjay", "Anjay"]
print(queue)
print(type(queue))
print(queue[-1])    #Anjay
print(queue[-4])    #Ajay

#append >> add element to the end of list
list2 = ["Apple", "Banana"]
list2.append("Orange")  #['Apple', 'Banana', 'Orange']
print(list2)
list2.append("Mango")   #['Apple', 'Banana', 'Orange', 'Mango']
print(list2)

playlist=[]
playlist.append("Sare jaha se achha")
playlist.append("Hindustan hamara")
print(playlist) #['Sare jaha se achha', 'Hindustan hamara']


