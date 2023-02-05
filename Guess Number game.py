#guess number from 1 - 20
import random

guessNumber = random.randint(1,20)
print("I'm thinking a number between 1 - 20, think about it!")

#6 try
for i in range(1, 7):
    userChoice = int(input())
    if int(userChoice) > guessNumber:
        print("Too high")
    elif int(userChoice) < guessNumber:
        print("Too Low")
    else:
        print("thats correct")
        break

if userChoice == guessNumber:
    print("Well done, you got it")
else:
    print("You run out of lives, the number is " + str(guessNumber))

