import random
tor = input("Enter a Number(RANGE): ")
if tor.isdigit():
    tor = int(tor)

    if tor <= 0:
        print("Enter a number greater than 0.")
        quit()
else:
    print("Enter a number.")
    quit()

random_number=random.randrange(1,tor)
guesses=0
while True:
    guesses+=1
    user_guess=input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please  type a number next time.")
        continue

    if user_guess==random_number:
        print("You guessed it right!")
        break
    else:
        if user_guess>random_number:
            print("You were above the number.")
        else:
            print("You were below the number.")
        

    
print("You got it in",guesses,"guesses")


