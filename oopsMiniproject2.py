import random
import string


password_len=8
charValue=string.ascii_letters+string.digits,string.punctuation
password= ""

for i in range(password_len):
    password+=random.choice(charValue)

print("Generated password is=",password)