import random


def introduction():
    print(
        "Welcome to Rock, Paper, Scissors! The goal of the game is to pick the option that counters your opponents option.\nFor example choosing rock will defeat scissors, scissors will defeat paper, and paper will defeat rock.\n\nSee if you can win three times in a row!\n"
    )


def get_player_choice():
    while True:
        choice = input(
            "Please make your choice by typing rock, paper, or scissors "
        ).lower()
        if choice.lower() in ("rock", "paper", "scissors"):
            return choice


def get_computer_choice():
    moves = ("rock", "paper", "scissors")
    computer_move = random.choice(moves)
    return computer_move


def determine_outcome(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("its a tie!")
        return "tie"

    if player_choice == "rock":
        if computer_choice == "scissors":
            print("Player wins!")
            return "player"
        elif computer_choice == "paper":
            print("Player loses!")
            return "cpu"
        else:
            print("Error detected!")

    if player_choice == "scissors":
        if computer_choice == "paper":
            print("Player wins!")
            return "player"
        elif computer_choice == "rock":
            print("Player loses!")
            return "cpu"
        else:
            print("Error detected!")

    if player_choice == "paper":
        if computer_choice == "rock":
            print("Player wins! Paper covers rock!")
            return "player"
        elif computer_choice == "scissors":
            print("Player loses! Paper is cut by scissors!")
            return "cpu"
        else:
            print("Error detected!")


def scoreboard(score):
    for key, value in score.items():
        print(key, value)


def play_again():
    while True:
        choice = input("Would you like to play again? (yes/no) ")
        if choice in ("yes", "no"):
            return choice


def main():
    score = {"player": 0, "cpu": 0, "tie": 0}
    introduction()
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        outcome = determine_outcome(player_choice, computer_choice)
        score[outcome] += 1
        scoreboard(score)
        if play_again() == 'no':
            print("\n Thank you for playing rock paper scissors! \nHere are the final scores!")
            scoreboard(score)
            break
            
        
        

if __name__ == "__main__":
    main()

# Welcome statement

# Explain the rules

# Ask the player if they would like to choose rock paper or scissors.

# The computer generates its own choice and than it is evaluated against the player

# The winner gets the points.
