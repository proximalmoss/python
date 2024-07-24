#mine a log file and find if it has 'python'
with open("log.txt") as f:
    content=f.read()
if "python" in content.lower():
    print("python is present")
else:
    print("python is not present")
#to find the line in which 'python' is present
content=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():
            print(content)
            print("python is present")
            print(i)
        i+=1