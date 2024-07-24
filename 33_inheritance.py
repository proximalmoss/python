#single inheritance
class Employee:
    company="Google"
    def showDetails(self):
        print("this is an employee")
class Programmer(Employee):
    def getLanguage(self,language):
        self.language=language
        print(f"the language is {self.language}")
    def showDetails(self):
        print("this is a programmer")
e=Employee()
e.showDetails()
p=Programmer()
p.getLanguage("python")
p.showDetails()
print(p.company)
#Multiple inheritance
class Employee:
    company="Visa"
    ecode=12
class Freelancer:
    company="Fiverr"
    level=0 #you only need an intial value for attribute in self
    def upgradeLevel(self):
        self.level=self.level+1
class Programmer(Employee,Freelancer): 
#if we reverse this company will be Fiverr becuause priority is given according to the order you write
    name="Rohit"
p=Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)
#multilevel inheritance
class Person:
    country="India"
    def takeBreak(self):
        print("I am breathing")
class Employee(Person):
    company="Honda"
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreak(self):
        print("I am an employee so I am breathing")
class Programmer(Employee):
    company="Fiverr"
    def getSalary(self):
        print("no salary programmer")
#super() method
    def takeBreak(self):
        super().takeBreak()
        print("I am programmer so I breath")
p=Person()
e=Employee()
pr=Programmer()
p.takeBreak()
e.takeBreak()
pr.takeBreak()
#class method
class Employee:
    company="camel"
    salary=100
    location="Delhi"
    #def changeSalary(self,sal):
    #    self.salary=sal #gives class salary as 100 NO CHANGE
#now to change class salary
    def changeSalary(self,sal):
        self.__class__.salary=sal #gives class salary also as 455
e=Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
#property decorators 
class Employee:
    company="Bharat Gas"
    salary=5600
    bonus=500
    totalsalary=6100
    @property
    def totalsalary(self):
        return self.salary+self.bonus
    @totalsalary.setter
    def totalsalary(self,value):
        self.bonus=value-self.salary
e=Employee()
print(e.salary)
print(e.bonus)
print(e.totalsalary)
e.bonus=700
print(e.totalsalary)
e.totalsalary=6100
print(e.bonus)
#operator overloading
class Number:
    def __init__(self,num1):
        self.num1=num1
    def __add__(self,num2):
        print("let's add")
        return self.num1*num2.num1 #USED FOR ALL KINDS OF OPERATORS 
n1=Number(4)
n2=Number(6)
sum=n1+n2
print(sum)
#other dunder methods 
