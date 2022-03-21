import random

choices = ["rock", "paper", "scissors"]

def checkChoices(player, com):
    if player == com:
        return "It's a tie!"
    elif (player == "rock" and com == "scissors") or (player == "paper" and com == "rock") or (player =="scissors" and com == "paper"):
        return "Player Wins!"
    elif (com == "rock" and player == "scissors") or (com == "paper" and player == "rock") or (com =="scissors" and player == "paper"):
        return "Computer Wins!"

def main():
    print("What is your choice? (rock, paper, scissors)")
    playerChoice = input()
    print(f'You chose {playerChoice}')
    comChoice = random.choice(choices)
    print(f'The computer chose {comChoice}')
    print(checkChoices(playerChoice, comChoice))

main()