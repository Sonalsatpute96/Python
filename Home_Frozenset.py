# frozen set >> immutable version of set., can not be changed added or removedO
# Use Cases
# frozenset is particularly useful when you need a collection of items that must remain constant and hashable, for example:

# As keys in dictionaries.
# As elements in other sets.
# In situations where immutability and integrity of data are important.
# overall, frozenset provides the functionality of a set with the added benefit of immutability,
#  making it useful for certain applications where the data should not change after creation.

s=([])
print(type(s))          #<class 'list'>
my_frozenset=frozenset([1,2,3,4,1,2])
print(my_frozenset)     #frozenset({1, 2, 3, 4})
print(type(my_frozenset))       #<class 'frozenset'>
# my_frozenset.add(11,12,13)
# print(my_frozenset)     #AttributeError: 'frozenset' object has no attribute 'add'
# print(my_frozenset.pop())           AttributeError: 'frozenset' object has no attribute 'pop'

# Creation
# You can create a frozenset using the frozenset() function. You can pass any iterable (such as a list, tuple, or set)
#  to this function to create a frozenset.

# Example of creating a frozenset
frozen = frozenset([1, 2, 3, 4])
print(frozen)
# Output: frozenset({1, 2, 3, 4})

# Immutability
# Once created, you cannot add or remove elements from a frozenset.

frozen = frozenset([1, 2, 3])
# The following lines will raise an AttributeError
# frozen.add(4)    # AttributeError
# frozen.remove(1) # AttributeError


# Hashability
# Because frozenset objects are immutable, they are hashable. This allows them to be used as keys in dictionaries or 
# as elements of other sets.

# Example of using frozenset as a dictionary key
d = {frozenset([1, 2, 3]): "value"}
print(d)
# Output: {frozenset({1, 2, 3}): 'value'}

# Example of using frozenset in a set
s = {frozenset([1, 2, 3]), frozenset([4, 5, 6])}
print(s)
# Output: {frozenset({1, 2, 3}), frozenset({4, 5, 6})}


# Methods
# frozenset supports most of the same methods as set, but without the methods that modify the set 
# (e.g., add, remove, discard, pop, and clear). Here are some common methods:

# copy(): Returns a shallow copy of the frozenset.
# difference(): Returns the difference of two or more sets as a new frozenset.
# intersection(): Returns the intersection of two or more sets as a new frozenset.
# union(): Returns the union of sets as a new frozenset.
# issubset(): Checks if the frozenset is a subset of another set.
# issuperset(): Checks if the frozenset is a superset of another set.

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

# Example of difference
print(a.difference(b))
# Output: frozenset({1, 2})

# Example of intersection
print(a.intersection(b))
# Output: frozenset({3})

# Example of union
print(a.union(b))
# Output: frozenset({1, 2, 3, 4, 5})