#to print "good day" using function
def func():
    name=input("enter your name")
    print("good day " + name)
func()
#or
def func1(name1):
        print("good day " + name1)
func1("hanan")
#default argument 
def func2(name='stranger'):
      print("good day "+ name)
func2("hanan")
func2()
    