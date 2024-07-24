#Q1 
name=input("enter name")
greeting=" good afternoon"
print(name+greeting)
#Q2
letter= '''Dear <|NAME|>
You are selected!
Date: <|DATE|>'''
NAME=input("enter name")
DATE=input("enter date")
letter=letter.replace("<|NAME|>",NAME)
letter=letter.replace("<|DATE|>",DATE)
print(letter)
#Q3 & Q4
str="This is a string with double  spaces"
doublespace=str.find("  ")
singlespace=str.replace("  "," ")
print(doublespace)
print (singlespace)
#Q5
ltr="Dear Harry, This python course is very nice.\nThanks!"
print(ltr)