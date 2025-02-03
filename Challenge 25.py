sentence = str(input("Write down a sentence here(lowercase only): "))
shift = int(input("Write down the amount of letters you want to shift in your sentence(max:25): "))
letter = "z"
output = ""
if shift > 25:
        print("Oops!! Remember the maximum number of letters is 25")

else:
    for move in sentence:
        
        if move == ' ':
            output += ' '

        elif move == 'z':
            output += chr(ord('`')+(shift))

        else:
            output += chr(ord(move)+shift)

        
print(output)

