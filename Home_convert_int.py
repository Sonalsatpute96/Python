#1. Converting to Integer (int())
num1_float=22.22
num1_int=int(num1_float)
print("Conversion of float to int",num1_int)
print(type(num1_int))

num2_string="22"
num2_int=int(num2_string)
print("Conversion of string to int",num2_int)
print(type(num2_int))

#2. Converting to Float (float())
num3_int=22
num3_float=float(num3_int)
print("Conversion from int to float=",num3_float)
print(type(num3_float))

num4_string="22"
num4_float=float(num4_string)
print("Conversion from string to float",num4_float)
print(type(num4_float))

#3. Converting to String (str())
num5_int=3
num5_str=str(num5_int)
print("int to string conversion",num5_str)
print(type(num5_str))

num6_float=3.14
num6_str=str(num6_float)
print("float to string conversion=",num6_str)
print(type(num6_str))

#4. Converting to Boolean (bool())

num7_int=3
num7_boolean=bool(num7_int)
print("int to boolean=",num7_boolean)
print(type(num7_boolean))

num8_str="Sonal Swapnil"
num8_boolean=bool(num8_str)
print("String to Boolean",num8_boolean)
print(type(num8_boolean))

num9_str="" #empty str convert to False and string presence convert to True
num9_boolean=bool(num9_str)
print("String to Boolean",num9_boolean)
print(type(num9_boolean))