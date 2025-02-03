animal = {'hippo' : 'calf',
           'horse' : 'foal',
            'dog' : 'pup',
            'kangaroo' : 'joey',
            'monkey' : 'infant',
            'owl' : 'owlet',
             'parrot' : 'chick',
            'rabbit' : 'bunny',
            'rat' : 'pup',
            'cow' : 'calf',
            'skunk' : 'kit',
            'sheep' : 'lamb'}

question = input("Enter the name of an animal that you want to know the baby name of: ")
big = ""
small = ""
print("The baby name of " + question + " is " + animal.get(question, "not on the list sorry."))

question2 = input("Do you want to add an animal and its baby on the list: ")

if question2 == "Yes" or "yes":
    big = input("What is the animal's name: ")
    small = input("What is its baby's name: ")
    animal[big] = small
    

else:
    print("Have a great day then!")
