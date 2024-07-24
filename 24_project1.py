#SNAKE WATER GUN GAME
import random
def game(comp,you):
    if (comp==you):
        return None
    elif (comp=="s"):
        if (you=="w"):
            return False
        elif (you=="g"):
            return True
    elif (comp=="w"):
        if (you=="g"):
            return False
        elif (you=="s"):
            return True
    else:
        if (you=="s"):
            return False
        elif (you=="w"):
            return True
print("computer turn: SNAKE(s),WATER(w),GUN(g)")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
else:
    comp='g'
you=input("your turn: SNAKE(s),WATER(w),GUN(g)")
a=game(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if(a==None):
    print("DRAW!")
elif(a==True):
    print("YOU WIN!")
else:
    print("you lose,better luck next time...")