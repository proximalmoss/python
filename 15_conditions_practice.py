#greatest number
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
num3=int(input("enter number 3"))
num4=int(input("enter number 4"))
if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num3
if(f1>f2):
    print(str(f1)+" is the greatest")
else:
    print(str(f2)+" is the greatest")
#question2
mark1=int(input("enter marks of subject1"))
mark2=int(input("enter marks of subject2"))
mark3=int(input("enter marks of subject3"))
if(mark1<33 or mark2<33 or mark3<33):
    print("fail")
elif((mark1+mark2+mark3)/3 <40):
    print("fail")
else:
    print("pass!")
#Q3 spam detector
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
#Q4 to check length of username ie length of string
username=input("enter your username")
length=len(username)
if(length<10):
    print("valid")
else:
    print("invalid")
#Q5 checking if given name is in list
names=["JJ","bhezinga","W2S","vikstar123","tbjzl","zerkaa","miniminter"]
name=input("enter a sideman")
if(name in names):
    print(name+ " is in the sidemen")
else:
    print(name+ "is not a sideman")