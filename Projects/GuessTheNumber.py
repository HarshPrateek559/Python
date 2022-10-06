print("Statement\tNumber\t\tAttempt\t\tRemain")

num = 30  # The number that is to be guessed.
atms = 4  # Number of attempts remain
rems = 1  # Number of attempts exhausted.
while (rems < 6):
    print("\t\t\t\t   "+str(rems)+"\t\t   "+str(atms))
    n = int(input("Input number\t  "))
    if n < num:
        if (rems < 5):
            # This condition checks whether player has another chance to play or not.
            print("Take a higher number next time.")
    elif n > num:
        if (rems < 5):
            # This condition checks whether player has another chance to play or not.
            print("Take a lower number next time.")
    else:
        print("Congratulations! You guessed the number")
        break
    atms = atms-1  # Decreasing No. of attempts
    rems = rems+1  # Increasing the number of attempts exhausted.

if rems == 6:
    # This condition executes incase the player lost the game.
    print("Sorry but you have lost the game. The number you had to guess was", num)
