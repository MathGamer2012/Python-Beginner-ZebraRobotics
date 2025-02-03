
string = str(input("Write down a sentence or word here: "))

vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')

new_message = ""

for letter in string:
    if letter not in vowels:
        new_message += letter


print("This is the new message after all the voewls have been removed: ", new_message)
