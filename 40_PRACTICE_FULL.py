#printing contents of folder in a list 
import os
print (os.listdir())
#variables and typecasting 
a=69
print(a)
print(type(a))
a=float(a)
print(type(a))
#strings
name="Hanan"
print(name)
n="Hello"
print(f"{n} {name}")
#slicing string 
print(name[0])
print(name[:3])
print(name[1:4])
print(name[::2]) #start to end with every other letter 
print(name[0:])
print(name[1:4:2]) # 1-4 at an interval of 2
print(len(name)) # length of string
#string functions YOU HAVE TO GIVE VARIABLE IS EQUAL TO 
print(len(name))
print(name.endswith("an")) #tells if string ends with the given character 
print(name.count("n")) #counts the given character 
print(name.capitalize()) #makes first letter of string capital
print(name.find("H"))#gives index of given character 
print(name.replace("Hanan","HI")) #repalces word 
#escape sequences 
str="Hanan is good. \n She \t is very good. \' HI \\ hello"
print(str)
#question
ltr=''' Dear <|NAME|>
You are selected!
Date: <|DATE|>'''
NAME= input("enter the name: ")
DATE= input("enter the date: ")
ltr=ltr.replace("<|NAME|>", NAME)
ltr=ltr.replace("<|DATE|>", DATE)
print(ltr)
#lists #directly sorts the list no variable to be given
L1=[20,69,72,10,4]
L1.sort() #ascending order to list
print(L1)
L1.reverse() #reverses the order of the list 
print(L1)
L1.append(8) #adds this to list
print(L1)
L1.insert(3,8)#adds 8 at 3rd index
print(L1)
L1.pop(2)#deletes element at index 2
print(L1)
L1.remove(10)#removes 20 from list 
print(L1)
#tuples #cannnot be altered so we put in another variable NEW TUPLE 
a=() #empty tuple
a=(1,) #tuple with one element MUST ADD COMMA 
a=(1,7,2)
print(a.count(1)) #returns the number of times 1 occurs in tuple
print(a.index(1)) #returns index of first occurance of 1
#sum of elements of list 
a=[2,4,6,8]
print(sum(a))
#cloning a list 
A=["a","b","c","d"]
B=A[:]
print(B)
#dictionary
a={"name":"Harry","from":"India","marks":[92,98,96]} #no variable required dict changed directly
print(a.items())
print(a.values())
print(a.keys())
a.update({"friend":"sam"})
print(a.get("name")) #returns value of this key
#typecasting 
print(list(a.keys()))
print(list(a.values()))
#sets
s={1,8,2,3}
print(len(s))
s.pop()
print(s)
s.remove(1)
print(s)
s.update({20,11})
print(s)
y={20,11} #for union there should be two sets
z=s.union(y)
print(z)
s1={2,3}
z1=z.intersection(s1)
print(z1)
z.clear()
print(z)
#simple translator
dict={"pankha":"fan","dabba":"box","vastu":"item"}
a=input("enter a hindi word: ")
print(dict)
print("the translation is: ", dict.get(a))
#nested dictionary
myDict={"fast":"in a quick manner","harry":"coder","marks":[1,2,5],"anotherdict":{"harry":"player"}}
print(myDict["anotherdict"]["harry"])
#condiitons 
a=22
if(a<9):
    print("greater")
else:
    print("lesser")
b=int(input("enter you age"))
if (b>=18):
    print("yes")
else:
    print("no")
#finding greatest
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
num4=int(input("enter the fourth number"))
if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num3
if(f1>f2):
    print(f"{f1} is the greatest")
else:
    print(f"{f2} is the greatest")
#spam text detector 
text=input("enter the text")
spam=False
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False
if(spam is True):
    print("this text is spam")
else:
    print(text)
#to check if given name is in list
names=["JJ","bhezinga","W2S","vikstar123","tbjzl","zerkaa","miniminter"]
name=input("enter a sideman")
if(name in names):
    print(name+ " is in the sidemen")
else:
    print(name+ "is not a sideman")
#While loop
i=0
while(i<5):
    print("hello")
    i+=1
#for loop for list
list=[1,7,8]
for i in list:
    print(i)
for i in range(0,7): #can use range
    print(i)
else:
    print("done")
#BREAK statement- to come out of loop when certain condition is encountered
for i in range(0,80):
    print(i)
    if i==3:
        break
#CONTINUE statement- to skip an iteration and then continue with the rest
for i in range(4):
    if(i==2):
        continue
    print (i)
#1-50 using while loop
i=0
while(i<=50):
    print(i)
    i+=1
#printing content of list using while loop 
fruit=['banana','watermelon','grapes','mango']
#i=0
#while(i<=len(fruit)):
    #print(fruit[i])
    #i+=1
for i in fruit: #same using for loop
    print(i)
#checking prime number
num=int(input("enter a number"))
prime=True
for i in range(2,num):
    if(num%i==0 and num!=2):
        prime=False
        break
if(prime is True):
    print("the given number is a prime number")
else:
    print("the given number is not a prime number")
#factorial of a number
num=int(input("enter the number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"factorial of the number is {fact}")
#patterns
#rectangle
n=5
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()
#left hand triangle 
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
#upside down left hand triangle 
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
#right hand triangle
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print
#full triangle 
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
#upside down full triangle
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
#diamond
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
#functions 
def fuc(): #printing good day using function
    name=input("enter your name")
    print(f"good day {name}")
fuc()
def fuc1(name1): #or another way
    print(f"good day {name1}")
fuc1("hanan")
#function using default argument 
def fuc2(name2="stranger"):
    print(f"good day {name2}")
fuc2("hanan")
fuc2()
#finding factorial using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#finding sum using recursion
def sum(n):
    if n==0 or n==1:
        return 1
    else:
        return sum(n-1)+n
print(sum(5))
#finding greatest of 3 numbers using function
def great(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
g=great(3,5,25)
print(f"the greatest among the 3 numbers is {g}")
#function to strip and remove word from string GIVING LIST 
def remove(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
s="   hanan is good   "
n=remove(s,"hanan")
print(n)
#to print in same line
print("Hello,", end=" ")
print("How",end=" ")
print("are",end=" ")
print("you?")
#function to print multiplication table
def print_multiplication_table(number):
  for i in range(1,11):
    product = number * i
    a= print(f"{number} * {i} = {product}")
  return a
print_multiplication_table(5)
#snake water gun
import random
def game(comp,you):
    if (comp==you):
        return None
    elif (comp=="s"):
        if (you=="w"):
            return False
        elif (you=="g"):
            return True
    elif (comp=="w"):
        if (you=="g"):
            return False
        elif (you=="s"):
            return True
    else:
        if (you=="s"):
            return False
        elif (you=="w"):
            return True
print("computer's turn: snake(s),water(w),gun(g)")
randno=random.randint(1,3)
if randno==1:
    comp="s"
elif randno==2:
    comp="w"
else:
    comp="g"
while True:
    you= input("your turn: snake(s),water(w),gun(g)")
    if(you=="s" or you=="w" or you=="g"):
        break
    else:
        print("invalid input")
a=game(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if(a==None):
    print("draw")
if(a==True):
    print("you win!")
else:
    print("you lose")
#file
f=open("sample.txt","w")
f.write("pls write this to the file")
f.close()
#to check whether the word twinkle is present in the file
f=open("twinkle.txt","r")
t=f.read()
if "twinkle" in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()
#to replace the word donkey in the file
with open("sample.txt","r") as f:
    content=f.read()
content=content.replace("donkey","%$#")
with open("sample.txt","w") as f:
    content=f.write(content)
#checking if two log files are same
with open("sample.txt","r") as f:
    f1=f.read()
with open("twinkle.txt","r") as f:
    f2=f.read()
if (f1==f2):
    print("the two files are same")
else:
    print("the two files are different")
#renaming files
import os
with open("sample.txt") as f:
    content=f.read()
with open("sample2.txt","w") as f:
    f.write(content)
os.remove("sample.txt")
#mining a logfile and checking if python is present 
with open("log.txt") as f:
    content=f.read()
if "python" in content.lower():
    print("python is present")
else:
    print("python is not present")
#checking which line python is present in
content=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(content)
            print("python is present")
            print(i)
        i+=1
#class attribute and instance attribute
class Employee:
    company="google"
    salary=5000
harry=Employee()
rajini=Employee()
print(harry.salary)
print(rajini.salary)
harry.salary=4000
print(harry.salary)
print(rajini.salary)
#the self parameter
class Employee:
    company="google"
    def getSalary(self):
        print("salary is 6K")
harry=Employee()
harry.getSalary
#in case you want to insert your own value in self
class Employee():
    company="google"
    def getSalary(self):
        print(f"salary is {self.salary}")
        print(f"company is {self.company}")
harry=Employee()
harry.salary=1000
harry.company="yt"
harry.getSalary()
#static method
class Hi():
    @staticmethod
    def greet():
        print("good morning")
harry=Hi()
harry.greet()
#__init__ constructor- used to run a method without being called
class Employee():
    def __init__(self):
        print("employee is created!")
harry=Employee()
#now applying to an actual problem
class Employee():
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("employee is created")
    def getDetails(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"subunit: {self.subunit}")
harry=Employee("harry",1000,"youtube")
harry.getDetails()
#class to find square,square root and cube of number
class Calculator():
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"the square of the number is {self.number**2}")
    def squareroot(self):
        print(f"the square root of the number is {self.number**0.5}")
    def cube(self):
        print(f"if the cube of the number is {self.number**3}")
    @staticmethod
    def greet():
        print("hello user!")
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
#train management system
class Train():
    def __init__(self,name,fare,seat):
        self.name=name
        self.fare=fare
        self.seat=seat
    def getStatus(self):
        print(f"name of train: {self.name}")
        print(f"number of seats available: {self.seat}")
    def getFare(self):
        print(f"fare: {self.fare}")
    def bookTicket(self):
        if self.seat>0:
            print(f"ticket has been booked! your seat number is {self.seat}")
            self.seat=self.seat-1
        else:
            print("sorry this train is full...")
intercity=Train("intercity express:1120",90,300)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.getFare()