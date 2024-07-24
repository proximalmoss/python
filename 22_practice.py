#function to find greatest of three numbers 
def great():
    a=int(input("enter number 1: "))
    b=int(input("enter number 2: "))
    c=int(input("enter number 3: "))
    if(a>b and a>c):
        return str(a) + " is greatest"
    elif(b>a and b>c):
        return str(b) + " is greatest"
    else:
        return str(c) + " is greatest"
print(great())
#another way
def max(num1,num2,num3):
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
m=max(1,2,3)
print("greatest number is "+ str(m))
#converting celsius to fharenheit 
def temp(c):
    tempreture=(c*9/5)+32
    return tempreture 
f=temp(0)
print("the tempreture in fharenheit is " + str(f))
#to print in same line
print("Hello,", end=" ")
print("How",end=" ")
print("are",end=" ")
print("you?")
#recursive function to calculate sum of n natural numbers
def sum(n):
    if n==0:
        return 0
    else:
        return sum(n-1)+n
print(sum(1))
#python function to print pattern GOTTA SEE THIS AGAIN
def pattern(n):
    for i in range(n):
        for j in range(i,n):
            a= print('*',end=" ")
        print()
print(pattern(3))
#function to strip and remove word from string GIVING LIST 
def remove(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
s="   Hanan is good     "
n=remove(s,"Hanan")
print(str(n))
#function to print multiplication table
def print_multiplication_table(number):
  for i in range(1,11):
    product = number * i
    a= print(f"{number} * {i} = {product}")
  return a
print_multiplication_table(5)
