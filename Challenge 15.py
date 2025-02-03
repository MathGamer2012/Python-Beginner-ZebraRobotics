word = str(input("Write down a sentence here: "))
counter = 0
for letter in word:
    if letter == "e":
        counter += 1 
        
print("This is the amount of characters in your sentence:",len(word))
print("The number of e's in your sentence are ", counter)
