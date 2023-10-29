import random
import math

player_wins = 0
player_losses = 0


def introduction():
    print(
        "Welcome to Rock, Paper, Scissors! The goal of the game is to pick the option that counters your opponents option. \n\nFor example choosing rock will defeat scissors, scissors will defeat paper, and paper will defeat rock.\n\nSee if you can win three times in a row!\n"
    )


def player_choice():
    player_choice = input(
        "Okay player, please press r to choose rock, press p for paper, and s for scissors.\n\nIf you wish to exit the game press e! \n \n"
    ).upper()
    if input == "R":
        print(
            "Okay player, you chose Rock! Lets see what your opponent chose! \n 5...\n 4...\n 3... \n 2... \n 1..."
        )
        player_choice = "ROCK"

    elif player_choice == "P":
        print(
            "Okay player, you chose Paper! Lets see what your opponent chose! \n 5...\n 4...\n 3... \n 2... \n 1..."
        )
        player_choice == "PAPER"

    elif player_choice == "S":
        print(
            "Okay player, you chose Scissors! Lets see what your opponent chose! \n 5...\n 4...\n 3... \n 2... \n 1..."
        )
        player_choice == "SCISSORS"

    elif player_choice == "E":
        print("Now exiting the game. Have a great day!")
    else:
        print(
            "Please make a valid selection. Press r for rock p for paper s for scissors or p for paper. "
        )


def computer_choice():
    print(
        "Computer challenger here. Prepare for defeat! Now calculating the ultimate strategy to defeat this nobody! \n"
    )
    moves = ("rock", "paper", "scissors")


def judge_outcome():
    if player_choice == "ROCK" & computer_choice == "PAPER":
        print("PLAYER LOSES PAPER COVERS ROCK!")
        player_losses += 1

    elif player_choice == "ROCK" & computer_choice == "SCISSORS":
        print("PLAYER WINS ROCK CRUSHES SCISSORS!")
        player_wins += 1

    elif player_choice == "ROCK" & computer_choice == "ROCK":
        print(
            "Judge: ITS A DRAW THE COMPETITORS will make another choice to break the tie!"
        )

    if player_choice == "SCISSORS" & computer_choice == "PAPER":
        print("PLAYER WINS SCISSORS CUTS PAPER!")
        player_wins += 1

    elif player_choice == "SCISSORS" & computer_choice == "SCISSORS":
        print(
            "Judge: ITS A DRAW THE COMPETITORS will make another choice to break the tie!"
        )

    elif player_choice == "SCISSORS" & computer_choice == "ROCK":
        print("PLAYER LOSES SCISSORS IS CRUSHED BY ROCK!")
        player_losses += 1

    if player_choice == "PAPER" & computer_choice == "PAPER":
        print(
            "Judge: ITS A DRAW THE COMPETITORS will make another choice to break the tie!"
        )
        player_wins += 1

    elif player_choice == "PAPER" & computer_choice == "SCISSORS":
        print("PLAYER LOSES AS SCISSORS CUTS PAPER!")
        player_losses = +1

    elif player_choice == "PAPER" & computer_choice == "ROCK":
        print("PLAYER WINS AS PAPER COVERS ROCK!")
        player_wins += 1
    else:
        print("ERROR Please talk to my creator!")


def main():
    introduction()
    player_choice()
    computer_choice()


# Welcome statement

# Explain the rules

# Ask the player if they would like to choose rock paper or scissors.

# The computer generates its own choice and than it is evaluated against the player

# The winner gets the points.


if __name__ == "__main__":
    main()
