#Three ways to declare string
str1='Hello'
str2="Hello,it is my 1'st program"  #1'st is valid in " "
str3="""World"""

#Basic string operation

str4=str1+str3
print("Final string=",str4)
len4=len(str4)
print("length of str4=",len4)

str4=str1+" "+str3
print("Final string=",str4)
len4=len(str4)
print("length of str4=",len4)

#slicing i.e accessing part of string and index start from '0'
#slicing is used in machine learning

str="Sonal"
print(str[0:4]) #ending index is not included
print(str[ :4]) #by default consider 1st index
print(str[2: ]) #by defaut consider last index

#slicing using negative index
# S o n a l
# -5 -4 -3 -2 -1 index pattern

print(str[-5:-1])

#string functions:

string1="i am a am coder"

print(string1.endswith("er")) #print true if ends with "er" substring
print(string1.capitalize()) #capitalize !st char of string
print(string1)

#string1=print(string1.capitalize())
#print(string1)
print(string1.replace("coder","singer")) #replace am with was
print(string1.find('am')) #give the 1st index of 1st occurence
print(string1.count("am")) #counts the occurence of the string
