# a set is a collection data type that is unordered, mutable, and does not allow duplicate elements. 
# Sets are used to store multiple items in a single variable. 
# Here's a brief overview of the properties and operations of sets:

# Sets are particularly useful for tasks that involve membership tests, 
# removing duplicates from a sequence, and mathematical operations like union and intersection.

# Properties:
# Unordered: The items in a set do not have a defined order.
# Immutable elements: The elements contained in a set must be immutable,
# i.e., they cannot be changed. However, the set itself is mutable.
# No duplicates: A set cannot have two items with the same value.

# Creating a Set:
# You can create a set by using curly braces {} or the set() function.

set1={1,2,3,4,1,2,3,4}
print(set1)             #{1, 2, 3, 4}
print(type(set1))       #<class 'set'

#Another way to create a set using a set keyword
set1=set([1,2,3,4,1,2,3,4])
print(set1)             #{1, 2, 3, 4}

# Basic Operations:
# Add elements: You can add an element to a set using the add() method.

set1.add("Sonal")
print(set1)     #{1, 2, 3, 4, 'Sonal'}

# Remove elements: You can remove an element using the remove() or discard() methods. 
# The remove() method will raise an error if the element does not exist, while discard() will not.

set1.discard("Sonal")
print(set1)         #{1, 2, 3, 4}
set1.discard("Swapnil")
print(set1)     #{1, 2, 3, 4} It doesn't throw an error even that elemnt is not present in the list.

set1.remove(1)
print(set1)         #{2, 3, 4}

# Check membership: You can check if an element is in a set using the in keyword.

print(4 in set1)        #True
print(5 in set1)        #False

# Set Operations:
# Union: Combines elements from both sets.
set1={1,2,3}
set2={3,5,6}
set3=set1.union(set2)
print(set3)     #{1, 2, 3, 5, 6}

# Intersection: Returns only the elements that are in both sets.
set3=set1.intersection(set2)
print(set3)     #{3}

# Difference: Returns the elements that are in the first set but not in the second
set3=set1.difference(set2)
print(set3)         #{1, 2}

# Symmetric Difference: Returns the elements that are in either set, but not in both.
set3=set1.symmetric_difference(set2)
print(set3)         #{1, 2, 5, 6}

fruits_set = {"apple", "banana", "cherry"}      #{'cherry', 'banana', 'apple'}
print(fruits_set)

fruits_set.add("Banana")
print(fruits_set)       #{'cherry', 'Banana', 'banana', 'apple'}

# remove(element): Removes the specified element from the set. 
# Raises a KeyError if the element is not found.

fruits_set.remove("cherry")
print(fruits_set)       #{'cherry', 'Banana', 'banana', 'apple'}

print("apple" in fruits_set)        #True

#discard(element): Removes the specified element from the set if it is present.
fruits_set.discard("Banana")
print(fruits_set)       #{'apple', 'banana'}

# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
fruits_set.pop()        #it doesn't takes an arguments
print(fruits_set)   #{'apple'}

# clear(): Removes all elements from the set.
fruits_set.clear()
print(fruits_set)       #set()

#copy()
s1={1,2,3}
s2=s1.copy()
print("***********s2*****",s2)          #***********s2***** {1, 2, 3}

#len()
print(len(s1))          #3


# s={1,2,3,[1,1]}     #TypeError: unhashable type: 'list'
s={1,2,3,(1,1)}
print(s)        #{3, 1, (1, 1), 2}

# print(s[0])-->TypeError: 'set' object is not subscriptable
# print(s[3])

print(1 in s)       #True

for i in s:
    print(i)
# Output
# 3
# 1
# (1, 1)
# 2
s.update("106") #update will not work with integers     {1, 2, 3, '0', '6', (1, 1), '1'}
print(s)

del s
# print(s)      NameError: name 's' is not defined

#Set operations
#Union: combines elements from two sets excluding duplicates
#Intersection: only common elements btw sets
#difference: return the elements that is present in first set and not in second
#symmetric difference: returns elements that are present in either of sets but not in both
s1 = {"hiking", "reading", "coding"}
s2 = {"coding", "photography", "travelling"}

#union
print(s1 | s2)      #{'reading', 'photography', 'coding', 'travelling', 'hiking'}

#intersection >> & 
print(s1 & s2)      #{'coding'}

#difference
print(s1 - s2)      #{'reading', 'hiking'}

#symmetric difference
print(s1^s2)








