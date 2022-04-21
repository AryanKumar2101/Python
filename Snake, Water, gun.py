import random

def gameWin(comp,You):
    if comp==You:
        return None
    elif comp=='s':
        if You=='w':
            return False
        elif You=='g':
            return True 
    elif comp=='g':
        if You=='s':
            return False
        elif You=='w':
            return True                 
    elif comp=='w':
        if You=='g':
            return False
        elif You=='s':
            return True 

print("Comp Turn:......")
randNo=random.randint(1,3) 
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'    
elif randNo==3:
    comp='g'

You=input("Your Turn: Snake(s) Water(w) Gun(g)")

a=gameWin(comp,You)

print(f"Compe Chose {comp}")
print(f"You Chose {You}")

if a==None:
    print("The game is a Tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")    
    