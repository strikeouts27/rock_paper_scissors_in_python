import random
import math

scoreboard = {"win": 0, "loss": 0, "tie": 0}


def introduction():
    print(
        "Welcome to Rock, Paper, Scissors! The goal of the game is to pick the option that counters your opponents option. \n\nFor example choosing rock will defeat scissors, scissors will defeat paper, and paper will defeat rock.\n"
    )


def get_player_choice():
    while True:
        user_choice = input(
            "Press r for rock, p for paper, s for sicssors or e for exit! "
        ).upper()
        if user_choice in ["R", "P", "S"]:
            if user_choice == "R":
                user_choice = "ROCK"
                print("this is a rock scenario")

            elif user_choice == "P":
                user_choice = "PAPER"

            elif user_choice == "S":
                user_choice = "SCISSORS"
            return user_choice
        elif user_choice == "E":
            exit()
        else:
            print("invalid entry please try again")


def get_computer_choice():
    print("Computer: formulating strategy to defeat the human")
    computer_choice_options = ("ROCK", "PAPER", "SCISSORS")
    computer_choices = random.choice(computer_choice_options)
    print(computer_choices + " test for computer_choice")
    return computer_choices


def judge_outcome(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Its a tie!")
        return "tie"

    elif player_choice == "ROCK":
        if computer_choice == "SCISSORS":
            print("Player wins! Rock crushes scissors!")
            return "win"

        if computer_choice == "PAPER":
            print("Computer wins! Paper covers rock!")
            return "loss"

    elif player_choice == "PAPER":
        if computer_choice == "ROCK":
            print("Player wins! Paper covers rock!")
            return "win"
        elif computer_choice == "SCISSORS":
            print("Player losses! Scissors cuts paper!")
            return "loss"

    elif player_choice == "SCISSORS":
        if computer_choice == "PAPER":
            print("Player wins! Scissors cuts paper!")
            return "win"
        elif computer_choice == "ROCK":
            print("Player loses! Rock crushes scissors!")
            return "loss"


def score_game(scoreboard):
    for key, value in scoreboard.items():
        print(f"{key}:{value}")


def play_again():
    while True:
        choice = input(
            "Would you like to play again? Press y for yes and n for no. "
        ).upper()
        if choice in ("yes, no"):
            return choice
        if choice == ("Y"):
            return choice
        elif choice == ("N"):
            return choice
        elif choice == ("YES"):
            return choice
        elif choice == ("NO"):
            return choice


def format_scoreboard(scoreboard):
    print("\n")
    print("Final totals: ")
    print("--------------")
    for key, value in scoreboard.items():
        print(f"{key}:{value}")
    print("Thank you for playing!")
    exit()


def main():
    introduction()
    scoreboard = {"win": 0, "loss": 0, "tie": 0}
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        outcome = judge_outcome(player_choice, computer_choice)
        scoreboard[outcome] += 1
        print(scoreboard)
        if play_again() == "N":
            break
    format_scoreboard(scoreboard)


main()

# Welcome statement

# Explain the rules

# Ask the player if they would like to choose rock paper or scissors.

# The computer generates its own choice and than it is evaluated against the player

# The winner gets the points.


if __name__ == "__main__":
    main()
