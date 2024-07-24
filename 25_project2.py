#ROCK PAPER SCISSOR GAME
import random
def game(comp,you):
    if(comp=='r'):
        if(you=='p'):
            return True
        elif(you=='s'):
            return False
    elif(comp=='p'):
        if(you=='s'):
            return True
        elif(you=='r'):
            return False
    elif(comp=='s'):
        if(you=='r'):
            return True
        elif(you=='p'):
            return False
    elif(comp==you):
        return None
    elif(you!='r' or you!='p' or you!='s'):
        return 0
print("computer's turn: ROCK(r),PAPER(p), SCISSOR(s)")
randno=random.randint(1,3)
if (randno==1):
    comp='r'
elif(randno==2):
    comp='p'
else:
    comp='s'

while True:
    you=input("your turn: ROCK(r),PAPER(p), SCISSOR(s)")
    if(you=='r' or you=='p' or you=='s'):
        break
    else:
        print("invalid input")
a=game(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if(a==None):
    print("DRAW!")
elif(a==True):
    print("YOU WIN!")
elif(a==False):
    print("you lose,better luck next time...")
