import random
word = ('coding' , 'programming', 'javascript', 'python', 'html')
shuffle = str(random.choice(word))
guess_word = ""
chance = 0
print("The length of the word is: ", len(shuffle))
guess = str(input("Guess a letter in the word: "))

while(chance < 5):
    if(shuffle.find(guess)!= -1):
        print("You guessed the correct letter!! That letter is in position: ", str(shuffle.find(guess)))
    else:
        print("Oops try again")
    guess = input("Guess a letter in the word: ")
    chance += 1
        
        
if(chance == 5):
    guess_word = str(input("What do you think is the word: "))

    if guess_word == shuffle:
        print("You guessed the correct word")

    else:
        print("Better luck next time")
                

    
    




