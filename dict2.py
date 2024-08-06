#Nested Dictionary
student={
    "Name":"Sonal",
    "Std":"SSC Board Exam",
    "Subject":{
        "Science":97,
        "Math":148,
        "History":95,
    },
    "Percentage":90.73,
}

print(student)
print(student["Subject"]["Math"])

print(len(student))
print(student.keys())   #return all the keys
print(student.values()) #return all the values
pair=list(student.items())  #return all the key:value pair item in the form of tuple
print(pair)
print(pair[0])

#print(student["name2"]) #return error
#print(student.get("name2")) #return name2=None
print(student.get("Percentage"))
new_dict={"Grade":"A+"}
student.update(new_dict)
print(student)