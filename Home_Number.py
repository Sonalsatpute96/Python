# Python is an object-oriented programming language, which means it deals with objects. 
# Everything in Python is an object, including numbers, strings, lists, and even functions. 
# Objects have attributes and methods associated with them.
# Numbers:

# Python supports various types of numbers, including integers, floating-point numbers, and complex numbers.

int_num=3
print(int_num)
print(type(int_num))

float_num=3.14
print(float_num)
print(type(float_num))

complex_num=3+4j
print(complex_num)
print(type(complex_num))

bool_num=True    #if write 1 consider the type as a "int"
print(bool_num)
print(type(bool_num))

#Set=A set is an unordered collection of unique elements. 
# Sets are mutable, meaning they can be modified after creation, but they cannot contain duplicate elements.

My_set={1,1,2,3,4,5}
print(My_set)
print(type(My_set))

My_dict={
    "Name":"Sonal",
    "CGPA":9.7,
    "age":28
    }
print(My_dict)
print(type(My_dict))


# Sequence:Strings in Python are sequences of characters enclosed in single, double, or triple quotes. 
# They support various operations such as concatenation, slicing, and formatting.

My_string="Sonal's"
print(My_string)
print(type(My_string))

#List=A list is a versatile data structure used to store collections of items.
#  Lists are mutable, meaning they can be modified after creation. Each item in a list is indexed, 
# and you can access elements by their index. 
# Lists can contain items of different data types, and they can also contain other lists (nested lists).

My_list=["Sonal",1,2.2,3+4j,True,{"Name":"Sonal"},["Arjun","Swapnil"],(1,2,3)]
print(My_list)
print(type(My_list))

#Tuple=A tuple in Python is a collection of ordered and immutable elements. 
# It is similar to a list, but unlike lists, tuples are immutable, 
# meaning their elements cannot be changed after creation. 
# Tuples are defined using parentheses () and can contain elements of different data types.

My_tuple=(1,2.2,3+4j,[2,3],("Sonal","Swapnil","Arjun"))
print(My_tuple)
print(type(My_tuple))

#NONE=None is a special constant representing the absence of a value or a null value.
# It is often used to indicate that a variable or an object does not have a meaningful value or 
# has not been assigned yet.

My_None=None
print(My_None)
print(type(My_None))