print("Welcome to muy Quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play..")
score = 0

answer = input("What does CPU stands for?")
if answer == "Central Processing Unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What does GPU stands for?")
if answer == "Graphics Processing Unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Where is Ukraine?")
if answer == "Europe":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does PSU stands for?")
if answer == "Power Supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got" + str(score)  +   "questions corrrect!")
print("You got" + str((score/4) * 100) + "%")