# Abstraction=Hiding the implentation details of a class and showing only the essential features to the user
# Encapsulation=Wrapping the data and function into the single unit

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("Car Started..")

c1=Car()
c1.start()

#output
# Car Started..it shows the essential methods not all other that is something is the encapsulation

# prctice que
# create Account class with two attribute balance,account no
# create a methods of debit creadit and balance

class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount, " is creadited")
        print(" Amount after credit=",self.get_balance())

    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount ," is debited")
        print("Amount after debit",self.get_balance())

    def get_balance(self):
        return self.balance

    
Acc1=Account(10000,221122)
Acc1.credit(1000)
Acc1.debit(500)
