# This program is an adaptation of Stone Paper Scissors in Python. The game would consist of 5 rounds, in each of which the player would have to choose between Stone, Paper, and Scissors.

# In the game:- stone would win over Scissors, scissors over paper, paper over stone.


import random

choose = ['stone', 'paper', 'scissors']

cscore = 0
pscore = 0

name = input("Enter the name of the player: ")

print(f'\tHello {name}!\n\tThis is Stone Paper Scissors. In this game you would have three options to choose from: Stone, Paper, and Scissors.\n\tTo play the game, you just have to press the button corresponding to your choice. Press:\n\t\t1 for Stone\n\t\t2 for Paper\n\t\t3 for Scissors\n\tIn this game, stone beats scissors, scissors beats paper and paper beats stone.\n\tThere will be 5 rounds at the end of which the winner would be announced. Good Luck😉')

def rounds():
    for i in range(5):
        print(f"\n\tRound {i + 1}")
        try: 
            n = int(input("\tEnter your choice: "))
            player = choose[n-1]
            computer = random.choice(choose)
            print(f"\tYour Choice: {player}\t Computer's Choice: {computer}")
            judgement(player, computer, i + 1)
        except Exception as e:
            print("\tInvalid Choice")
            continue


def judgement(player, computer, i):
    global cscore, pscore

    if player == "stone":
        if computer == 'paper':
            cscore = cscore + 1
            print(f"\tRound {i} winner: Computer")
        elif computer == 'scissors':
            pscore = pscore + 1
            print(f"\tRound {i} winner: {name}")
        else: 
            print("\tThis round is a tie!!!")
    
    elif player == "scissors":
        if computer == 'stone':
            cscore = cscore + 1
            print(f"\tRound {i} winner: Computer")
        elif computer == 'paper':
            pscore = pscore + 1
            print(f"\tRound {i} winner: {name}")
        else: 
            print("\tThis round is a tie!!!")
    
    elif player == "paper":
        if computer == 'scissors':
            cscore = cscore + 1
            print(f"\tRound {i} winner: Computer")
        elif computer == 'stone':
            pscore = pscore + 1
            print(f"\tRound {i} winner: {name}")
        else: 
            print("\tThis round is a tie!!!")
    
    print(f"\tYour Score: {pscore}\t\tComputer's Score: {cscore}")

rounds()

print(f"\n\tFinal Score\n\tYour Score: {pscore}\t\tComputer's score: {cscore}")
if pscore > cscore:
    print("\n\tYou Win!!!!!")
elif cscore > pscore:
    print("\n\tYou lose!!!")
else:
    print("There is a tie! NO ONE WINS!!!!")