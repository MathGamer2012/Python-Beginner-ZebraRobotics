import random
import sys
num = random.randint(1,10) 
guess = int(input("Guess a number between 1 and 10: "))
turn = 1



while(turn != 3):
        if(guess == num):
                print("You guessed the correct number!!")
                sys.exit("Better Luck Next Time!!")
        else:
                print("Try again!!")
                guess = int(input("Guess a number between 1 and 10: "))
        turn += 1

    
if(turn == 3):
         sys.exit("Better Luck Next Time!!")
   

    





    

    
    
