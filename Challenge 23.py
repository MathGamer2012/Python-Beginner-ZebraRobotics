name = input("Write your name here: ")
score = int(input("Write your score here: "))
name2 = input("Write your name here: ")
score2 = int(input("Write your score here: "))
name3 = input("Write your name here: ")
score3 = int(input("Write your score here: "))
name4 = input("Write your name here: ")
score4 = int(input("Write your score here: "))
name5 = input("Write your name here: ")
score5 = int(input("Write your score here: "))
List1 = [name, score]
List2 = []
List2.append(List1)
List1 = [name2, score2]
List2.append(List1)
List1 = [name3, score3]
List2.append(List1)
List1 = [name4, score4]
List2.append(List1)
List1 = [name5, score5]
List2.append(List1)

List2 = sorted(List2, key=lambda x: x[1], reverse = True)
print("This is the list of marks ordred in descending order: ",List2)
