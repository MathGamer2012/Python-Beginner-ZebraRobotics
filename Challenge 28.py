def menu():
    print("Select one of the options: \n 1. Lookup animal babies \n 2. Add animal and baby \n 3. Delete animal and baby")
    option = int(input("Write the number of your option here: "))
    big = ""
    small = ""
    question2 = ""
    question3 = ""
    question4 = ""
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
    
    if option == 1:
        question = input("Enter the name of an animal that you want to know the baby name of: ")
        print("The baby name of " + question + " is " + animal.get(question, "not on the list sorry."))

    if option == 2:
       big = str(input("What is the animal's name: "))
       small = str(input("What is its baby's name: "))
       print(big + " and " + small + " have been added to the list")
       animal[big] = small
       print("Here is the list of animals and its babies after you added",big,"and", small,"on the list \n", animal)

    if option == 3:
        print("Here is the list of animals and its babies", animal)
        question3 = input("Enter the name of the animal that you want to remove: ")
        del animal[question3]
        print("Here is the list of animals and its babies after you removed" ,question3, "from the list \n" , animal)
        
        
        



menu()













    

