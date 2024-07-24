#printing multiplication table
num=int(input("enter the number"))
for i in range(1,11):
    print(str(i) + "X" + str(num) + "=" + str(num*i))
#greeting
l1=["harry","soham","sachin","rahul"]
for i in l1:
    if i.startswith("s"):
        print("hello " + i)
#problem 1 with while loop
i=1
num=int(input("enter the number"))
while(i<=10):
    print(str(i) + "X" + str(num) + "=" + str(num*i))
    i=i+1
#checking prime number
num=int(input("enter a number"))
prime=True
for i in range(2,num):
    if(num%i==0 and num!=2):
        prime=False
        break
if (prime is True):
    print("number is prime")
else:
    print("number is not prime")
#finding sum of n natural numbers using while loop
n= int(input("enter a number"))
sum=0
i=0
while(i<=n):
    sum=sum+i
    i=i+1
print("sum= " + str(sum))
#to calculate factorial of a number
num=int(input("enter a number"))
fact=1
for i in range (1,num+1):
    fact=fact*i
print(f"the factorial of the number is {fact}")
#printing star patten
n=5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

