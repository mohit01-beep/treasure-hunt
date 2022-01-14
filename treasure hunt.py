from replit import clear
gameover = False
while not gameover:
    clear()
    print("Welcome to treasure island")
    start= input("where do you want to go?: type left or right ").lower()
    if start=="left":
        choice1=input("There's a lake over there, do you want to swim or do you want to wait for boat?: type swim or wait ").lower()
        if choice1== "wait":
            choice2=input("you reached island safely, now there's 3 gate with different colour. Which colour do you want to choose?: 'yellow' or 'red' or 'blue' ").lower()
            if choice2=='yellow':
                over=input("you found the treasure. congratulations, do you want to play again?")

            elif choice2=='red':
                over=input('that room was full of fire.Game over, do you want to coninue?')
            elif choice2=='blue':
                over=input('That room was full of werewolves. Game over, do you want to continue?yes or no')        
            else:
                over=input('you chose a door that doesn\'t exist, do you want to continue')
        else:
            over=input("you're eaten by an sea monster, Game over, Do you want to continue? yes or no")
    else:
        over=input("Game over. you fell in a well which was covered with grass, do you want to continue? yes or no")

if over== 'no':
    gameover=True
