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

print("The baby name of " + question + " is " + animal.get(question, "not on the list sorry."))
