#Tuples are ordered collection of elements, heterogenous
#Tuples are immutable
# In Python, a tuple is an immutable sequence type that can hold a collection of items.
# Several built-in functions and methods are commonly used with tuples. 
# Here’s a detailed explanation of these functions:

t=()
print(type(t))          #<class 'tuple'>
tuple1=(1,2.2,2+7j,"Sonal",[1,2,3],{"1":"one","2":"two"})
print(tuple1)       #(1, 2.2, (2+7j), 'Sonal', [1, 2, 3], {'1': 'one', '2': 'two'})
print(tuple1[0])    #1
print(tuple1[2])    #(2+7j)

#tuple1[0]=2         #TypeError: 'tuple' object does not support item assignment
# print(tuple1)

print(tuple1.count(2))  #0
print(tuple1.count(2.2))  #1

# Built-in Tuple Functions
# 1.len(tuple)
# Description: Returns the number of items in the tuple.
print(len(tuple1))      #6

# 2.max(tuple)
# Description: Returns the largest item in the tuple.
#print(max(tuple1))      #TypeError: '>' not supported between instances of 'complex' and 'float'
t=("Sonal","Arjun")
print(max(t))           #Sonal
#print(sum(t))           #TypeError: unsupported operand type(s) for +: 'int' and 'str'
t=(1,2,3,7,4,99,1,2)
print(max(t))           #99

#list to tuple conversion
print("**********tuple**********",tuple[t])     #**********tuple********** tuple[1, 2, 3, 7, 4, 99, 1, 2]

# 3.min(tuple)
# Description: Returns the smallest item in the tuple.
print(min(t))       #1

# 4.sum(tuple)
# Description: Returns the sum of all items in the tuple.
print(sum(t))       #119

# 5.sorted(tuple)
# Description: Returns a sorted list of the tuple’s items.
print(sorted(t))        #[1, 1, 2, 2, 3, 4, 7, 99]

# 6.tuple(iterable)
# Description: Converts an iterable (like a list) into a tuple.
#list to tupple conversion
list1=[1,2,"sonal",{"1":"One"}]
print(tuple(list1))     #(1, 2, 'sonal', {'1': 'One'})

# 7.all(): Returns True if all items in the tuple are true.

my_tuple = (1, 2, 3)
print(all(my_tuple))  # Output: True

# 8.any(): Returns True if any item in the tuple is true.

my_tuple = (0, 1, 2)
print(any(my_tuple))  # Output: True


#****************************************************************************************************
# Tuple Methods(only 2 methods are there)

# 1.tuple.count(value)
# Description: Returns the number of times a specified value appears in the tuple.
tuple1=(1,2.2,2+7j,"Sonal",[1,2,3],{"1":"one","2":"two"})
print(tuple1.count(2.2))        #1

#2.index(x, [start[, end]]): Returns the index of the first occurrence of x in the tuple. 
# Optional arguments start and end specify a subsequence to search.
t=(1,2,3,7,4,99,1,2)
print(t.index(99))      #5
print(t.index(7,1,6))      #3

#*******************************************************************************************************
# Apart from these methods, tuples support several operations and functions:
# Indexing: Access an element by its index.
t=(1,2,3,7,4,99,1,2)

print(t[0])     #1
print(t[3])     #7

#Slicing: Access a range of elements.
print(t[:4])        #(1, 2, 3, 7)
print(t[2:])        #(3, 7, 4, 99, 1, 2)
print(t[::-1])      #(2, 1, 99, 4, 7, 3, 2, 1)
print(t[::-2])      #(2, 99, 7, 2)
print(t[-1:-3])     #()
print(t[-3:-1])     #(99, 1)

# Concatenation: Combine tuples using the + operator.
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)        #(1, 2, 3, 4, 5, 6)

# Repetition: Repeat a tuple using the * operator.
print(t1*3)         #(1, 2, 3, 1, 2, 3, 1, 2, 3)
print((t1+t2)*3)    #(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

# Membership: Check if an element exists in the tuple using the in operator.
print(2 in t1)  #True
print(2 in t2)  #False

# Length: Get the number of elements in a tuple using the len() function.
print(len(t1))      #3

# Iteration: Iterate over the elements of a tuple using a for loop.
for element in t1:
    print(element)
# output
# 1
# 2
# 3

# different topic
list1 = [2, 3, 4, 4, 4, 5, 5]
s = set(list1)
print(list(s))      #[2, 3, 4, 5]

for i in s:
    print(i)
# output=
# 2
# 3
# 4
# 5
















