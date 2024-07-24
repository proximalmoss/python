#class attribute and instance attribute
class Employee:
    company="google"
    salary=100
harry=Employee()
rajini=Employee()
print(harry.salary)
print(rajini.salary)
harry.salary=30
print(harry.salary)
print(rajini.salary)
#self parameter
class Employee:
    company="google"
    def getSalary(self):
        print("salary is 100k")
harry=Employee()
harry.getSalary()
#same as above but we want to insert our value
class Employee:
    company="google"
    def getSalary(self):
        print(f"salary is {self.salary}")
        print(f"company is {self.company}")
harry=Employee()
harry.salary=100
harry.company="yt" 
#1st priority is instance attribute then is class attribute if instance attribute is not given
harry.getSalary()
#static method
class Hi:   
    @staticmethod
    def greet():
        print("good morning")
harry=Hi()
harry.greet()
#__init__ constructor
#used to run method without being called
class Employee:
    def __init__(self):
        print("employee is created!")
harry=Employee()
# now applying to an actual problem
class employee:
    company="google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("employee is created!!")
    def getSalary(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"subunit: {self.subunit}")
harry=employee("Harry",100,"Youtube")
class employee:
    company="google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("employee is created!")
    def getSalary(self):
        print(f"name: {self.name}")
        print(f"salary: {self.salary}")
        print(f"subunit: {self.subunit}")
harry=employee("Harry",100,"Youtube")
harry.getSalary()