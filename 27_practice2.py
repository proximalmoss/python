#to make a copy of the text file "this.txt"
with open ("log.txt") as f:
    content=f.read()
with open ("copy.txt","w") as f:
    f.write(content)
#to check if content of two files is same
with open("log.txt") as f:
    f1=f.read()
with open("copy.txt") as f:
    f2=f.read()
if(f1==f2):
    print("files are identical")
else:
    print("they are different files")
#renaming file
import os
with open("copy.txt") as f:
    content=f.read()
with open("renamed_by_python","w") as f:
    f.write(content)
os.remove("copy.txt")