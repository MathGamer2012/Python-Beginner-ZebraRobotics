
team = {}


def add(team1,score1):
    team[team1] = score1
    

def updateScore(team1, score1):
    team[team1] += score1


def inquire(team1):
    return team[team1]  
    
def delete(team1):
    question4 = team1
    del team[team1]

while(True):
    print("Select one of the options: \n 1. Add Team \n 2. Update Team Score \n 3. Inquire Team \n 4. Delete Team \n 5. Quit")
    choice = int(input("Your Choice: "))

    if choice == 1:
        team1 = str(input("Write the name of your team: "))
        score1 = int(input("What is the score of " + team1 + ": "))
        add(team1,score1)
        print(team)

    if choice == 2:
        question3 = str(input("Which team do you want to add the points to: "))
        question2 = int(input("How many points do you want to add: "))
        updateScore(question3, question2)
        print(team)

    if choice == 3:
        question = str(input("Write your team name here: "))
        score1 = inquire(question)
        print("The score of",question, "is", score1)
        

    if choice == 4:
        question4 = str(input("Which team do you want to delete: "))
        delete(question4)
        print(team)

    if choice == 5:
        break

        


    


