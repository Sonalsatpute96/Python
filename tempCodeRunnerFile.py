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
print(a)  