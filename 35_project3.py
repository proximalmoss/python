import random
randno=random.randint(1,100)
guess=0
user=None
while(user!=randno):
    user=int(input("guess a number between 1 to 100: "))
    guess+=1
    if (user==randno):
        print("you guessed correct!")
    else:
        print("you guessed wrong...")
        if(user>randno):
            print("guess a smaller number")
        else:
            print("guess a larger number")
print(f"you guessed the number in {guess} guesses")
with open ("highscore.txt","r") as f:
    highscore=int(f.read())
if (guess<highscore):
    print("you have broken the highscore!")
with open ("highscore.txt","w") as f:
    f.write(str(guess))