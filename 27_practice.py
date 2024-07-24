#to check whether the word twinkle is present in the file
f=open("twinkle.txt","r")
t=f.read()
if "twinkle" in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()
# to replace the word donkey in a file
with open("sample.txt","r") as f:
    content=f.read()
content=content.replace("donkey","%$&^%")
with open("sample.txt","w") as f:
    content=f.write(content)
#same as above but we have to create a list of such words
words=["pedo","fat","donkey"]
with open("sample.txt") as f:
    content=f.read()
for word in words:
    content=content.replace(word,"%$&*^")
    with open("sample.txt","w") as f:
        content=f.write(content)