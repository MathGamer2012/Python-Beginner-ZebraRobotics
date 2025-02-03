sentence = str(input("Write down a sentence here(lowercase only): "))
output = ""
for shift in sentence:
    output += chr(ord(shift)+1)
print(output)
