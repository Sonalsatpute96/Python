prices=[10,20,30,40,50,60]
doubled_prices=[]
for i in prices:
    doubled_prices.append(i*2)      #[20, 40, 60, 80, 100, 120]
print(doubled_prices)

doubled_price = [price * 2 for price in prices]
print(doubled_price)                #[20, 40, 60, 80, 100, 120]

names=["sonal","swapnil","arjun"]
print([name.capitalize() for name in names])    #['Sonal', 'Swapnil', 'Arjun']

number=[1,2,3,4,5]
print([num1**3 for num1 in number])         #[1, 8, 27, 64, 125]

str1="document1.ppt"
print(str1.split(".")[-1])          #ppt

#conditional list comprehension

email_address = ["aj@gmail.com", "sj@yahoo.com", "rj@yahoo.com", "mj@gmail.com"]
print([email for email in email_address if email.endswith("yahoo.com")])        #['sj@yahoo.com', 'rj@yahoo.com']

#Nested list comprehension
pair=[]
for x in [1,2,3]:
    for y in [4,5,6]:
        print([x,y])
        pair.append([x,y])

print(pair)

#print([x,y] for x in [1,2,3] for y in [4,5,6])---><generator object <genexpr> at 0x0000016A506192A0>

#list as stack and queue
#stack >> last in first out principle > the last element added to the stack will be the first one to be removed
Stack1=[]
Stack1.append("A")
Stack1.append("B")
Stack1.append("C")
Stack1.append("D")
print(Stack1)
print(Stack1.pop())
print(Stack1.pop())
print(Stack1.pop())
print(Stack1.pop())

#Queue >> FIFO>> FIRST IN FIRST OUT
#ORDERLY SEQUENTIAL MANNER
# TWO ENDS

from collections import deque
my_collection=deque()
my_collection.append("customer 1")
my_collection.append("customer 2")
my_collection.append("customer.3")
print(my_collection)

while my_collection:
    customer=my_collection.pop()
    print("serving",customer)

# ['A', 'B', 'C', 'D']
# D
# C
# B
# A
# deque(['customer 1', 'customer 2', 'customer.3'])
# serving customer.3
# serving customer 2
# serving customer 1

from queue import Queue
Print_Quque=Queue()
Print_Quque.put("A")
Print_Quque.put("B")
Print_Quque.put("C")
Print_Quque.put("D")

while not Print_Quque.empty():
    Print_job=Print_Quque.get()
    print(Print_job)

print_queue = Queue()

print_queue.put("Print job 1")
print_queue.put("Print job 2")
print_queue.put("Print job 3")


while not print_queue.empty():
    print_job = print_queue.get()
    print("printing",print_job)

