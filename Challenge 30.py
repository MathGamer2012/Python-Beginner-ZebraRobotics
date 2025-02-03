import random

def game():

    if guess == num:
        print("Congrats you won")

    elif guess > num:
        print("Your guess is too high")

    elif guess < num:
        print("You guess is too low")


num = random.randint(1,10)
print(num)
guess = int(input("What do you think is the number: "))


game()
