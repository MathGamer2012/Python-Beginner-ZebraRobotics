import random

num = random.randint(1,10)
print(num)
chance = 0

def game():    
        if guess == num:
            print("Congrats you won")

        elif guess > num:
            print("Your guess is too high")

        elif guess < num:
            print("You guess is too low")
            
while(chance != 3):
    guess = int(input("What do you think is the number: "))
    game()
    chance += 1  
          
     

