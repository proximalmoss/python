#first example
fruits=['apple','mango','banana']
for index,fruit in enumerate(fruits):
    print(index,fruit)
    print (f"{index+1} {fruit}")
#normal way of doing this 
marks=[12,56,32,98,12,45,14]
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("hi")
    index+=1
#same problem using enumerate
marks=[12,56,32,98,12,45,14]
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("hi")
