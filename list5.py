#check for pallindrome
#eg="maam"  "pop"   "racecar"

list1=[1,"Sonal",2,2,"Sonal",1]
list2=list1.copy()
list2.reverse()
if(list1==list2):
    print("Given list is pallindrome")
else:
    print("Given list is not pallindrome")