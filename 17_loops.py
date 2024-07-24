#while loop
i=0
while(i<5):
    print("hello")
    i=i+1
#for loop
l=[1,7,8]
for item in l:
    print(item)
#for loop in range
for i in range(0,7):
    print(i)
#1-50 using while loop
i=0
while(i<=50):
    print(i)
    i=i+1
#printing content of list using while loop
fruit=['banana','watermelon','grapes','mango']
i=0
while(i<len(fruit)):
    print(fruit[i])
    i=i+1
#same with for
for item in fruit:
    print(item)
#break statement
for i in range(0,80):
    print(i)
    if i==3:
        break
#continue statement 
for i in range(4):
    if i==2:        #can be used to print even and odd numbers also
        continue
    print(i)
#pass statement
l=[1,7,8]
for item in l:
    pass