#basic try
try:
    a=int(input("enter a number: "))
    print(f"multiplication table of {a}: \n")
    for i in range (1,11):
        print(f"{a} x {i} = {a*i}")
except Exception as e:
    print(e)
print("some imp lines of code")
print("end of program")
#different exceptions 
try:
    num=int(input("enter an integer: "))
except ValueError:
    print("number entered is not an integer")
except IndexError:
    print("index error")
#there are different funtions for different types of errors