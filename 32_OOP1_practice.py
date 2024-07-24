#to store information of few employees working at microsoft
class Programmer:
    company="microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getDetails(self):
        print(f"name: {self.name}")
        print(f"product: {self.product}")
harry=Programmer("Harry","Skype")
sam=Programmer("Sam","Github")
harry.getDetails()
harry.company="yt" #TRIAL
print("company: " + harry.company)
#class to find square, sqaure root and cube
class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"square is {self.number**2}")
    def squareroot(self):
        print(f"sqaureroot is {self.number**0.5}")
    def cube(self):
        print(f"cube is {self.number**3}")
#adding static method Q4 to greet user
    @staticmethod
    def greet():
        print("hello!")
Calculator.greet()
n=int(input("enter number: "))
o=int(input("choose option 1.SQAURE 2.SQUAREROOT 3.CUBE"))
a=Calculator(n)
if o==1:
    a.square()
elif o==2:
    a.squareroot()
elif o==3:
    a.cube()
else:
    print("invalud input")
#class train with options 
class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print(f"name of train: {self.name}")
        print(f"number of seats available: {self.seats}")
    def getFare(self):
        print(f"fare: {self.fare}")
    def bookTicket(self):
        if self.seats>0:
            print(f"ticket has been booked! your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry this train is full...")
intercity=train("intercity express:1120",90,300)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.getFare()
