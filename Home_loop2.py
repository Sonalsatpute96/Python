n=int(input("Enter a no to check is no is prime or not="))
flag=False
for i in range(2,n,1):      #must be n not"n+1"
    if n%i==0:
        flag=True
        break
if flag:
    print("not prime")
else:
    print("prime")
# Enter a no to check is no is prime or not=19
# prime


no=1234
n=4

for i in range(n,0,-1):
    print(i)
