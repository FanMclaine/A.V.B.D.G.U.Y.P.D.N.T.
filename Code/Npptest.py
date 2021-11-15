import random
number=random.randint(1,200)

print("=== Welcome to a dungeon game! Press [ENTER] on how to play! === ")
input("")
print()
print(" Mechanics of the game: Choose dooors from 1 to 3 inorder to escape the dungeon.")
print(" Rules: There are no rules (yet). Enjoy!")
print(" Press [ENTER] to continue")
print()
input("")
print("__________________________________________________________________")
print()
print("You see three doors; pick one (Use 1,2, and 3 keys)")
Doors= input("|1| |2| |3| > ")
if Doors == "1":
    print()
    print(" You found a sleeping monster! we need to get sneaky to find the exit!")
    print()
    print(" Get sneaky by  typing 'pneumonoultramicroscopicsilicovolcanoconiosis'! ")
    print()
    long=input("")
    if long == "pneumonoultramicroscopicsilicovolcanoconiosis":
        print()
        print("Great job! You've earned 200 golds and escaped the dungeon!")
        print("Ending got: Sneeeaaakkyyy (Neutral)")
        input("")
    else:
        print("Oh no! you've awaken the monster!")
        print("Game over!")
        input("")
elif Doors == "2":
    print()
    print("You found piles of golds and diamonds! and a exit!")
    print("Ending got: Lucky day (Good)")
    input("")
elif Doors == "3":
    print()
    print("You are greeted by a speaking statue.")
    print("'Hello there mortal, oh? wanna escape this dungeon? not too fast mortal!' said the speaking statue")
    print()
    input("")
    print()
    print()
    print("Ralsei: Bloody hell innit the fokin statue put a spell on us, oh bollocks")
    input("")
    print()
    print("WHAHAHAHAHA, fellow mortals, i would like you to read my mind; Im thinking of a number between 1-200.")
    input("")
    print("If you guessed my number; you can escape this dungeon. If you did not guessed my number; I will put your soul in an endless loop!")
    print()
    input("")
    print("Ralsei: Oi bruv dont fokin mess with us innit")
    input("")
    print("'Oooooh brave!' says the statue 'Well i should start the game now! whahahahahha!")
    print()
    guess = int(input("Ralsei: Bloody hell innit choose a fokin number> "))
    while guess != number:
        if guess < number:
            print("'Ha! PUSSIES' says the statue")
        else:
            print("'Ha! PUSSIES' says the statue")
    print("'Congratulation mortals! im going to lead you to the exit'")
    print("Ending got: Rude Ralsei (Bad)")
   
   #Welll 
   #We are near to 69 
   #yay!
#removed cringer
