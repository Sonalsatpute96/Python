#string is a sequence of character
#characterd represented using numerical values
#ASCII (7 bits) and UNICODE (16 bits)
#UTF-8, UTF 16 >> popular encoding schemes

#ASCII representation

char='A'
print(ord(char))
print(ord("Z"))
print(ord("a"))
print(ord("z"))

print(chr(65))
print(chr(90))
print(chr(97))
print(chr(122))

#OUTPUT=
# 65
# 90
# 97
# 122
# A
# Z
# a
# z

#UNICODE representation #omega
print('\u03A9')
print('\u03A3')
print('\u0973')

# output=
# Ω
# Σ
# ॳ

print(chr(977))         #ϑ

string1="Sonal"
print(string1)
print(type(string1))

print("I'm a good student")

#concatenation of string ?? combining of two strings
str1="Hello"
str2="World"
print(str1+","+str2)
print(str1+str2)
print(str1+" "+str2)

print(str1+">"+"Sonal")
print("Sonal"+" swapnil"+" Bendhale")
#output=
# Hello,World
# HelloWorld
# Hello World
# Hello>Sonal
# Sonal swapnil Bendhale

#Extract a string

string2="I am a fast learner"
print(string2[0:4])
print(string2[1:10])
print(string2[0:len(string2)])
# output=
# I am
#  am a fas
# I am a fast learner
string3="Sonal"
print(string3[-1])
print(string3[-2])
print(string3[-1:-3])
print(string3[-3:-1])
print(string3[::-1])
print("String3=",string3[:6])     #Sonal
#output
# l
# a

# na
# lanoS

strr="2201010101011"
print(strr[::2])    
print(strr[::-1])
print("LENGTH=",len(strr))  #LENGTH= 13
#Output
# 2000001
# 1101010101022

#strings are immutable
# s="Sonal"
# s[0]="M"
# print(s)    #TypeError: 'str' object does not support item assignment

print("Sonal"+"ARJUN")

#modification of string
string4="I am a teacher"
print(string4.replace("teacher","developer"))       #I am a developer
print(string4)    # I am a teacher 

text = "BRB, TTYL, LOL"
print(text.replace("BRB","Be right back").replace("TTYL","Talk to you later").replace("LOL","Laughter of loud"))
print(text)
#output=
# Be right back, Talk to you later, Laughter of loud
# BRB, TTYL, LOL

print("String Function")
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.casefold())
#output
# brb, ttyl, lol
# BRB, TTYL, LOL
# Brb, ttyl, lol
# brb, ttyl, lol

print("Center=",string1.center(2))
print("Count=",text.count("B"))
print(string1.encode())
#output=
# Center= Sonal
# Count= 2
# b'Sonal'

print("endswith=",string1.endswith("al"))
print(string1.expandtabs())
print(text.expandtabs())
print("find",string1.find("o"))
print("format=",string1.format())
#output=
# endswith= True
# Sonal
# BRB, TTYL, LOL
# find 1
# format= Sonal-->below proper example is given

print("index",string1.index("n"))
print("Formatmap",text.format_map(1))
print("isdecimal",string1.isdecimal())
print("isdigit",string1.isdigit())
print("islower",text.islower())
print("isupper",text.isupper())
#output
# index 2
# Formatmap BRB, TTYL, LOL
# isdecimal False
# isdigit False
# islower False
# isupper True

print(string1.isalpha())
print(string1.isprintable())
print(string1.isidentifier())
print(string1.isspace())
print(string2.isspace())
print(string1.istitle())
#output=True
# True
# True
# False
# False
# True

print(string1.isupper())    #false
print(string1.join("Sonal"))    #SSonaloSonalnSonalaSonall
print(string1.ljust(2)) #Sonal(don't know???)
print(text.lstrip())        #BRB, TTYL, LOL--->?????
print(string1.maketrans("s","o"))   #{115: 111}--->ASCII VALUES
print(string1.partition("o"))       #('S', 'o', 'nal')
print(string1.removeprefix("S"))    #onal--->just mention prefix 
print(string1.removesuffix("l"))    #Sona---->need to mention last char only
print(text.removesuffix("LOL"))     #BRB, TTYL,
print(string1.rfind("nal"))         #2--->the index where substring found
print(string1.rindex("al"))         #3--->return highest index where substring 

print(text.rjust(1))
print(text.rpartition("LOL"))
print(string1.rpartition("n"))
# output
# BRB, TTYL, LOL
# ('BRB, TTYL, ', 'LOL', '')
# ('So', 'n', 'al')
# ['BRB,', 'TTYL,', 'LOL']
# BRB, TTYL, LOL

text1 = "I am Is A Student"
print(text1.swapcase())     #i AM iS a sTUDENT

sentence="I am a sonal bendhale"
print("am" in sentence)     #True

search_word="sonal"
if search_word in sentence:
    print("Word is present")
else:
    print("Word is not present")        #Word is present

email="sonalsatpute96gmail.com"
if "@" in email:
    print("valid email")
else:
    print("Invalid email")      #Invalid email

document = "some_file.pdf"
if ".pdf" in document:
    print("its a pdf file")
else:
    print("Not")        #its a pdf file

string5="Sonal"
string6="sonal"
print(string5==string6)     #false
print(string5==string1)     #True
print(string6.lower()==string5.lower())     #true
print(string5.lower()==string1.lower())

str1 = "Hello"
str2 = "hello"


print(str1.lower() == str2.lower())

user_list1=["Sonal","Swapnil","Arjun"]
user_name="Saurabh"
if user_name in user_list1:
    print("User is already exist")
else:
    print("This is new user name")

product_key="P123"
new_key=input("Enter a key=")
if product_key==new_key:
    print("Same key")
else:
    print("Different key")


#STRING ORDERING=

Name=["Sonal","Arjun","pranavi"]        #['Arjun', 'Sonal', 'pranavi']--->p small letter
print(sorted(Name))

Name2=["c","a","x","Z"]
print(sorted(Name2))        #['Z', 'a', 'c', 'x']--->Z capital letter

#common string operations

input_str = "      Sonal        "
print(input_str.strip())        #The strip() function in Python is used to remove any leading and trailing whitespace characters 
#(spaces, tabs, newlines) from a string. 
#It does not affect any whitespace characters that are in the middle of the string.

string7="Sonal   "
print(string7.strip())      #Sonal

#string splitting

string8="C,C++,PYTHON,SQL,HTML,CSS"
print(string8.split(","))           #['C', 'C++', 'PYTHON', 'SQL', 'HTML', 'CSS']
print(type(string8.split()))        #<class 'list'>
string9="1soanl1swapnil"
print(string9.split("1"))           #['', 'soanl', 'swapnil']

data = "Ajay,     data science, teacher"
print(data)         #Ajay, data science, teacher
teacher_info  = data.split(',')
print(teacher_info)     #['Ajay', ' data science', ' teacher']
name = teacher_info[0]
sub = teacher_info[1]
des = teacher_info[2]
print(name)         #Ajay
print(des.strip())      #teacher--->This list comprehension iterates through each element produced by split(',')
#and applies strip() to remove any leading or trailing spaces before storing them in teacher_info.
print(sub.strip())      #data science

#Escape sequence >> special combination of characters used within a strings

Address='''Jagdamba Housing Society,House No=11,sector N0=4
,Moshi Pradhikaran,Pune-412105'''
print(Address)          #Jagdamba Housing Society,House No=11,sector N0=4
#,Moshi Pradhikaran,Pune-412105

Address='''Jagdamba Housing Society ,\nHouse No=11,\nsector N0=4,\nMoshi Pradhikaran,\nPune-412105'''
print(Address)
# Jagdamba Housing Society ,
# House No=11,
# sector N0=4,
# Moshi Pradhikaran,
# Pune-412105

Languages="C \t C++ \t JAVA \t PYTHON"
print(Languages)        #C        C++     JAVA    PYTHON

file_path = "C:\\USERS\\DOWNLOAD\\FILES.txt"
print(file_path)            #C:\USERS\DOWNLOAD\FILES.txt

#\' single quote escape
str1 = 'I can\'t believe it\'s a friday'
print(str1)         #I can't believe it's a friday

#Carriage return \r >> moves the cursor to the beginning of line

print("Hello, I am \rAjay. I am going to Delhi")        #Ajay. I am going to Delhi

# In Python, \r (carriage return) moves the cursor to the beginning of the current line, effectively allowing you to overwrite text
#  on the same line. Here's how the output will be interpreted:

# "Hello, I am \rAjay. I am going to Delhi"

# "Hello, I am " will be printed first.
# \r moves the cursor to the beginning of the line.
# Ajay. will then overwrite "Hello, I am ", resulting in "Ajay.".
# The rest of the string " I am going to Delhi" will be printed as is.

#string formatting >> creating string with placeholder for variables 
username = "Shyam"
greeting = f"hello {username}, how are you?"        #hello Shyam, how are you?
print(greeting)

# greeting = f"hello {username}, how are you?": Constructs a string greeting using an f-string.
# The expression {username} inside the f-string is replaced with the value of the variable username, 
# resulting in "hello Shyam, how are you?".

name = "Sonal"
greeting = "Hello %s! wish you a wonderful day" %name
print(greeting)     #Hello Sonal! wish you a wonderful day

#.format
template = "Hello, {} Welcome to {}"
message = template.format("Sonal", "Python")
print(message)          #Hello, Sonal Welcome to Python

my_course="Python Course"
duration=" 4 months"
print(f"I selected {my_course} and duration of{duration} ") #I selected Python Course and duration of 4 months

name3="Sonal Bendhale"
age=28
print(f"My name is {name3} and I am {age} years old")