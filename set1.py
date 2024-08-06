#set is cllection iof the unordered items 
#Sets is mutable but its elements are immutable
#As the elements of set are immutable we cannot pass list and dict to set
#Each elements in the list mmust be unique.
#boolen->int->float->string->tuple all are immutable
#only list and dictionary are the mutable(can update can change)
#list and dict never stored in immutable datatype

set1={1,2.2,"Sonal",(1,2,3),1}
print("Set1=",set1)     #Ignore duplicate elements.

empty_set_syntax=set()  #syntax of empty set
print("empty_set_syntax",empty_set_syntax)

empty_set_syntax.add("Swapnil") #add element to set
print(empty_set_syntax)

set1.remove(2.2)       #remove the elemnt from set
print(set1)

empty_set_syntax.clear()    #empties the set
print(empty_set_syntax)

set1.pop()      #remove the random element
print(set1)
