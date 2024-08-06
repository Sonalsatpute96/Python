#iterator is an object that is used to iterate over iterable objects
#list, tuple, dict, string, sets

for i in "sonal":
    print(i)

# s
# o
# n
# a
# l

list1=[1,2,3,4,"Sonal"]
for i in list1:
    print(i)
#  1
# 2
# 3
# 4
# Sonal   

# for i in 5:
#     print(i)        #Exception has occurred: TypeError
                      #'int' object is not iterable
s="Hello"
# iter(s)             #IndentationError: expected an indented block after 'for' statement on line 14

for i in s:
    print(i)
# H
# e
# l
# l
# o

a = iter(s)
print(a)        #<str_ascii_iterator object at 0x000002A979A577F0>?????????????????????
print(next(a))  #H
print(next(a))  #e
print(next(a))  #l
print(next(a))  #l
print(next(a))  #0

for i in s:
    print(i)

# H
# e
# l
# l
# o

str="Arjun"
a=iter(str)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# A
# r
# j
# u
# n

a=iter([11,22,33,44,55])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# 11
# 22
# 33
# 44
# 55

a=iter((1,2.2,3+4j))
print(next(a))
print(next(a))
print(next(a))
# 1
# 2.2
# (3+4j)

a=iter({1,2,3,4})
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# 1
# 2
# 3
# 4

a={
    "Name":"Sonal",
    "email_id":"sonalsatpute96@gmail.com"
}
# print(next(a))
# print(next(a))
# Exception has occurred: TypeError
# 'dict' object is not an iterator

#generator functions
#generator is a type of function which does not return a single value, instead returns an iterator object


