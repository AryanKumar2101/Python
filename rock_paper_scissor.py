import random

user_wins=0
computer_wins=0

options = ["rock","paper", "scissor"]

while True:
    user_input=input("Choose Rock/Paper/Scissor or Type Q to quit.").lower()

    if user_input== "q":
        print("Goodbye!")
        break

    if user_input not in options:
        continue

    random_number=random.randint(0, 2)
    computer_picks=options[random_number]
    print("Computer picked", computer_picks +".")

    if user_input=="rock" and computer_picks=="scissor":
        print("You Won!")
        user_wins+=1
    elif user_input=="paper" and computer_picks=="rock":
         print("You Won!")
         user_wins+=1
    elif user_input=="scissor" and computer_picks=="paper":
         print("You Won!")
         user_wins+=1
    else:
        print("Computer Wins!")
        computer_wins+=1
        

    print("You Won", user_wins, "times and computer wins", computer_wins, "times.")
    
    



