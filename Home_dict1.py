#dictionary is a data structure that stores data as key-value pair
#Unordered, Keys are unique and immutable

d={}
print(type(d))
d={
    "Name":"Sonal",
    "email-id":"sonalsatpute96@gmail.com",
    "contact no":"7385524460",
}
print(d)

# <class 'dict'>
# {'Name': 'Sonal', 'email-id': 'sonalsatpute96@gmail.com', 'contact no': '7385524460'}

print(d["Name"])
print(d["email-id"])
d["Name"]="Sonali"
print(d["Name"])
print(d)    #{'Name': 'Sonali', 'email-id': 'sonalsatpute96@gmail.com', 'contact no': '7385524460'}

# Sonal
# sonalsatpute96@gmail.com
# Sonali

d[1]="One"
print(d)    #{'Name': 'Sonali', 'email-id': 'sonalsatpute96@gmail.com', 'contact no': '7385524460', 1: 'One'}

d={1:"One"}
print(d)    #{1: 'One'}

d={2.2:"Float Value"}
print(d)    #{2.2: 'Float Value'}

d={True:"Boolean TYPE"}
print(d)    #{True: 'Boolean TYPE'}

# d = {#:"abc"}     #error
# d = {@:"abc"}     #error
#d = {[1, 2,3]:"abc"}        #TypeError: unhashable type: 'list'
#d = {(1, 2,3):"abc"}        #TypeError: unhashable type: 'list'
print(d)

# d = {{1, 2,3}:"abc"}    #TypeError: unhashable type: 'set'
# print(d)
# d = {{"key":123}:"abc"}
# print(d)            #TypeError: unhashable type: 'dict'

d={
    "Name":"Sonal",
    "email-id":"sonalsatpute96@gmail.com",
    "contact no":"7385524460",
    "Name":"Saurabh",       #{'Name': 'Saurabh', 'email-id': 'sonalsatpute96@gmail.com', 'contact no': '7385524460'}
    "Name":"Swapnil"        #{'Name': 'Swapnil', 'email-id': 'sonalsatpute96@gmail.com', 'contact no': '7385524460'}}
}
print(d)
d["Name"]="Sonal Bendhale"
print(d)        #{'Name': 'Sonal Bendhale', 'email-id': 'sonalsatpute96@gmail.com', 'contact no': '7385524460'}

dict1={
    "Name":["Sonal","Swapnil","Saurabh"],
    "Course":["Python","mern stack","Data science"]
}
print(dict1)        #{'Name': ['Sonal', 'Swapnil', 'Saurabh'], 'Course': ['Python', 'mern stack', 'Data science']}
print(d['Name'][1]) #o -->To print the value associated with the key 'Name' at index 1 in dictionary d, you can use the 
print(dict1["Course"][1])       #mern stack
print(dict1["Course"][2])       #Data science
dict1["Name"]="Arjun"
print(dict1)        #{'Name': 'Arjun', 'Course': ['Python', 'mern stack', 'Data science']}

dict1["date_of_start"] = "15th March"
print(dict1)

dict1["Name"]="Sonal"
print(dict1) #{'Name': 'Sonal', 'Course': ['Python', 'mern stack', 'Data science'], 'date_of_start': '15th March'}

del dict1["Course"]
print("del for perticular element=",dict1)  #del for perticular element= {'Name': 'Sonal', 'date_of_start': '15th March'}

del(dict1)
#print(dict1)    #NameError: name 'dict1' is not defined. Did you mean: 'dict'?

#print(type(dict1))--->NameError: name 'dict1' is not defined. Did you mean: 'dict'?

#******************************************************************************************************************
# All dictionary methods
# 1. dict.clear()
# Removes all items from the dictionary.

dict1 = {"name": ["Ajay", "Bijay", "Sanjay"], "course": ("ds", "ml")}
print(dict1)
print(dict1.clear())    #None

# Key Differences:

# Effect on Dictionary:

# del can be used to delete specific items or the entire dictionary (del dictionary[key] or del dictionary).
# clear() is used specifically to empty the dictionary (dictionary.clear()).

# Return Value:
# del statement does not return any value. It modifies the dictionary in place.
# clear() also does not return any value; it modifies the dictionary in place by removing all items.

# Use Cases:
# Use del when you want to selectively remove specific items or the entire dictionary.
# Use clear() when you want to empty the dictionary without deleting it.

#2. dict.copy()
dict1={1:"one",2:"Two"}
dict_copy=dict1.copy()
print(dict_copy)        #{1: 'one', 2: 'Two'}

# 3. dict.fromkeys(iterable, value=None)
# Creates a new dictionary with keys from iterable and values set to value.

keys={1,2,3}
d=dict.fromkeys(keys,"Alphabets")
print(d)        #{1: 'Alphabets', 2: 'Alphabets', 3: 'Alphabets'}

d=dict.fromkeys(keys,"numbers")
print(d)        #{1: 'numbers', 2: 'numbers', 3: 'numbers'}

# 4. dict.get(key, default=None)
# Returns the value for key if key is in the dictionary, else default.

d={'A':65,66:"B"}
print(d.get('A'))       #65
print(d.get(66))        #66

# 5. dict.items()
# Returns a view object that displays a list of dictionary's key-value tuple pairs.

dict1={
    "Name":"Sonal",
    "conatct_no":7385524600
}
print(dict1.items())    #dict_items([('Name', 'Sonal'), ('conatct_no', 7385524600)])

# 6. dict.keys()
# Returns a view object that displays a list of all the keys in the dictionary.
print(dict1.keys())     #dict_keys(['Name', 'conatct_no'])

# 7. dict.pop(key, default=None)
# Removes the specified key and returns the corresponding value. If the key is not found, default is returned 
# if provided, otherwise KeyError is raised.

print(dict1.pop("conatct_no"))      #7385524600
print(dict1)                        #{'Name': 'Sonal'}

# 8. dict.popitem()
# Removes and returns a key-value pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order.

dict1={"1":"1","2":"2","3":"3"}
print(dict1.popitem())
print(dict1.popitem())
print(dict1.popitem())
# output=('3', '3')
# ('2', '2')
# ('1', '1')

# 9. dict.setdefault(key, default=None)
# If key is in the dictionary, returns its value. If not, inserts key with a value of default and returns default.

dict1={"1":"1","2":"2"}
dict1.setdefault("1","One")
dict1.setdefault("3","Three")
print(dict1)        #{'1': '1', '2': '2', '3': 'Three'}

# 10. dict.update([other])
# Updates the dictionary with the key-value pairs from other, overwriting existing keys. 
# other can be another dictionary or an iterable of key-value pairs

dict1={"1":"1","2":"2"}
dict1.update({"1":"one","3":"Three"})       #more than 2 key value pair expected && put curly brace inside()
print(dict1)        #{'1': 'one', '2': '2', '3': 'Three'}

# 11. dict.values()
# Returns a view object that displays a list of all the values in the dictionary.
print(dict1.values())       #dict_values(['one', '2', 'Three'])

# 12. dict.__contains__(key)
# Returns True if the dictionary has the specified key, otherwise False.

d = {'a': 1, 'b': 2}
print('a' in d)  # Output: True
print('c' in d)  # Output: False


# 13. dict.__delitem__(key)
# Removes the item with the specified key. Equivalent to del d[key].
 
d = {'a': 1, 'b': 2}
del d['a']
print(d)  # Output: {'b': 2}


# 14. dict.__getitem__(key)
# Returns the value associated with the specified key. Equivalent to d[key].

d = {'a': 1, 'b': 2}
print(d['a'])  # Output: 1

# 15. dict.__setitem__(key, value)
# Sets the value of the specified key. Equivalent to d[key] = value.

d = {'a': 1, 'b': 2}
d['a'] = 3
print(d)  # Output: {'a': 3, 'b': 2}

#dictionary comprehension
# Dictionary comprehension in Python is a concise way to create dictionaries. 
# It allows you to generate dictionary key-value pairs dynamically in a single line of code, 
# using a syntax similar to list comprehensions.

# The basic syntax for dictionary comprehension is:
# {key_expression: value_expression for item in iterable}

# Here’s a breakdown:

# key_expression and value_expression define the key and value for each entry in the dictionary.
# for item in iterable loops over each item in the iterable.
#1.Basic Dictionary Comprehension:
square={x:x**2 for x in range(1,10)}
print(square)       #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#2.Using Conditional Logic:
square={x:x**2 for x in range(1,10) if x%2==0}
print(square)       #{2: 4, 4: 16, 6: 36, 8: 64}

#3.Combining Two Lists into a Dictionary:
keys=["1","2","3"]      #[] is to use
values=["One","two","Three"]
pairs={keys[i]:values[i] for i in range(len(keys))}
print(pairs)        #{'1': 'One', '2': 'two', '3': 'Three'}

#4.Transforming Existing Dictionary:
dict1={
    "A":65,
    "B":66,
    "C":67
    }
inverted_dict1={values:keys for keys,values in dict1.items()}
print(inverted_dict1)       #{65: 'A', 66: 'B', 67: 'C'}

students = ['Arun', 'Ajay', 'Bob']
marks = [80, 95, 90]
dict1={students[i]:marks[i] for i in range(len(students))}
print(dict1)        #{'Arun': 80, 'Ajay': 95, 'Bob': 90}

for i in zip(students,marks):
    print(i)
#output=
# ('Arun', 80)
# ('Ajay', 95)
# ('Bob', 90)

print({students:marks for students,marks in zip(students,marks)})       #{'Arun': 80, 'Ajay': 95, 'Bob': 90}

user_id = [1, 2, 3]
user_name = ["a21", "a22", "a33"]
print({user_id:user_name for user_id,user_name in zip(user_id,user_name)})    #{1: 'a21', 2: 'a22', 3: 'a33'}

students={
    "classroom 1":{"Name":"Sonal","department":"computer"},
    "classroom 2":{"Name":"Saurabh","department":"Mechanical"},
    "classroom 3":{"Name":"Shubham","Department":"Civil"}
}
print(students)         #{'classroom 1': {'Name': 'Sonal', 'department': 'computer'}, 'classroom 2': 
# {'Name': 'Saurabh', 'department': 'Mechanical'}, 'classroom 3': {'Name': 'Shubham', 'Department': 'Civil'}}
print(students["classroom 1"])      #{'Name': 'Sonal', 'department': 'computer'}

#Dictionary view objects
print(students.keys())      #dict_keys(['classroom 1', 'classroom 2', 'classroom 3'])
print(students.values())    #dict_values([{'Name': 'Sonal', 'department': 'computer'}, 
                            #{'Name': 'Saurabh', 'department': 'Mechanical'}, {'Name': 'Shubham', 'Department': 'Civil'}])
print(students.items())     #dict_items([('classroom 1', {'Name': 'Sonal', 'department': 'computer'}), 
#('classroom 2', {'Name': 'Saurabh', 'department': 'Mechanical'}), ('classroom 3', {'Name': 'Shubham', 'Department': 'Civil'})])





