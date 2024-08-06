#Dictionaries are used to store data values in "key":value pair form
#Dictionaries are unordered,mutable(changeable),Dont allow duplicate data

dict1={
    "Name":"Sonal",
    "Course":"Python full stack",
    "marks":98.56,
    "Grade":"A",
    "lang":("Python","html","css","javascript"),

}
print("Lets Display Dictionary=",dict1)
print(dict1["Name"])
print(dict1["Course"])
print(dict1["marks"])
print(dict1["Grade"])
print(dict1["lang"])

dict1["Surname"]="Bendhale"
dict1["Grade"]="A+"
print(dict1)

empty_dict={}
print("Example of empty dictionary=",empty_dict)
empty_dict["name"]="Sonal"
print(empty_dict)