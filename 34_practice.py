#Q1
class C2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class C3dvec(C2dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
v2d=C2dvec(1,3)
v3d=C3dvec(1,9,7)
print(v2d)
print(v3d)
#Q2
class Animals:
    animaltype="mammal"
class Pets(Animals):
    color="white"
class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow")
d=Dog()
d.bark()
#Q3
class Employee:
    salary=1000
    increment=1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment=sai/self.salary
e=Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement=2000
print(e.increment)
#Q4 class complex numbers with overloaded operators 
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary+c.imaginary)
    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} -{-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"
    def __mul__(self,c):
        mulreal= self.real*c.real-self.imaginary*c.imaginary
        mulimg=self.real*c.imaginary+self.imaginary*c.real
        return Complex(mulreal,mulimg)
c1=Complex(1,3)
c2=Complex(1,5)
print(c1+c2)
print(c1*c2)
#Q5 addition and multiplication of vectors 
class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1=""
        for i in self.vec:
            str1 += f"{i}a{index}+"
            index+=1
        return str1
v1=Vector([1,4,6])
print(v1)