# Loops in Python are used to execute a block of code repeatedly until a specified condition is met. 
# Python provides two primary loop constructs:

# 1.for loop
# 2.while loop
# Let's dive into each of these in detail.

# 1.for Loop
# The for loop in Python is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string) or 
# other iterable objects.
# Syntax
# python

# for variable in sequence:
#     # code to execute

fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)  
# Output=
# apple
# banana
# cherry

# Using range()
# The range() function is commonly used with for loops to generate a sequence of numbers.

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4
# PS C:\U

# Looping through a string
for character in "Sonal":
    print(character)
# S
# o
# n
# a
# l
# PS C:\Users\Swapnil>

# Looping through a dictionary
dict1={"Name":"Sonal","Course":"Python full stack"}
for key,value in dict1.items():
    print(key,value)
# Name Sonal
# Course Python full stack

# while Loop
# The while loop in Python is used to repeatedly execute a block of code as long as the condition is true.

# Syntax

# while condition:
#     # code to execute

count1=1
while count1<=5:
    print(count1)
    count1=count1+1
# 1
# 2
# 3
# 4
# 5

# Infinite Loop
# A while loop can become an infinite loop if the condition never becomes false. 
# To stop an infinite loop, you can use the break statement.

while True:
    print("This is an infinite loop")
    break
# output
# This is an infinite loop

# Control Statements
# Python provides control statements to alter the normal flow of a loop.

# break=The break statement is used to exit the loop immediately, regardless of the loop's condition.

for i in range(10):
    if(i==5):
        break
    print(i)
# 0
# 1
# 2
# 3
# 4

# continue
# The continue statement is used to skip the current iteration and proceed to the next iteration of the loop.

for i in range(10):
    if(i==5):
        continue
    print(i)
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9

for i in range(10):
    if(i%2==0):
        continue
    print(i)
# 1
# 3
# 5
# 7
# 9

# The loop for i in range(2, n + 1, 2): iterates through even numbers from 2 up to 
# 𝑛
# n (inclusive). Here's a breakdown of the loop components:

# 2: The starting value of the range.
# n + 1: The ending value of the range (exclusive). Since ranges in Python do not include the endpoint, adding 1 makes it inclusive of 
# 𝑛
# n.
# 2: The step value, indicating the increment between each iteration.
# This means the loop will iterate over the sequence: 2, 4, 6, ..., up to 
# 𝑛
# n (if 
# 𝑛
# n is even).

n = 10
for i in range(2, n + 1, 2):
    print(i)
# Output:
# 2
# 4
# 6
# 8
# 10

# Print all even numbers till n except multiples of 7
print("Print all even numbers till n except multiples of 7")
n=int(input("Enter a no till u want the table of 2="))
for i in range(2,n+1,2):
    if i%7==0:
        continue
    print(i,end=" ")
# Enter a no till u want the table of 2=100
# 2 4 6 8 10 12 16 18 20 22 24 26 30 32 34 36 38 40 44 46 48 50 52 54 58 60 62 64 66 68 72 74 76 78 80 82 86 88 90 92 94 96 100




# else Clause with Loops
# Both for and while loops can have an else clause. The else part is executed when the loop terminates normally 
# (not by a break statement).

print(" else Clause with Loops")
for i in range(10):
    print(i)
else:
    print("Loop is completed")

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Loop is completed

count1=2
while count1<=6:
    print(count1)
    count1=count1+1
else:
    print("Loop is completed")

# 2
# 3
# 4
# 5
# 6
# Loop is completed

# Why do we need else when both of the above programs output is same?
# Else can be used efficiently with break statement. Else will not be executed if your loop is broken by a break statement. 
# Else gets executed iff the for/ while loop condition becomes false

n=int(input("Enter a no="))
for i in (2,n,1):
    if(n%2==0):
        break
else:
    print("Odd Number")
# Enter a no=45
# Odd Number

n=2
while n<5:
    if n==6:
        break
    print(n,end="  ")
    n=n+1
else:
    print("else is also printed")
#   2  3  4  else is also printed  

# Predict the Output
i=1
while i<5:
    if i == 3:
        break
    print(i,end= " ")
    i = i + 1
else:
    print("Else is also printed")
# output=
# 1 2

# Nested Loops
# Loops can be nested inside other loops. The inner loop runs completely for every iteration of the outer loop.

for i in range(3):
    for j in range(3):
        print(f'i={i},j={j}')       #f is compulsory else will get the output like i={i},j={j}

# i=0,j=0
# i=0,j=1
# i=0,j=2
# i=1,j=0
# i=1,j=1
# i=1,j=2
# i=2,j=0
# i=2,j=1
# i=2,j=2

# Looping through Data Structures
# Looping through a List

Names=["Arjun", "Sonal","Swapnil"]
for list in Names:
    print(list)

# Arjun
# Sonal
# Swapnil

# Looping through a Tuple
Tuple1=("Pyhton","C","c++",".net")
for lang in Tuple1:
    print(lang)

# Pyhton
# C
# c++
# .net

# Looping through a Set
set1={1,2,3,1,2,3}
for set in set1:
    print(set)
# 1
# 2
# 3

# Looping through a Dictionary
dict1={
    "Name":"Sonal",
    "Course":"Python Full Stack Developer"}
for keydict,valuedict in dict1.items():
    print(keydict,valuedict)

# Name Sonal
# Course Python Full Stack Developer

# Comprehensions
# List comprehensions provide a concise way to create lists. They can be used as a more readable and 
# compact alternative to using loops.

square =[square**2 for square in range(10)]
print(square)

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
