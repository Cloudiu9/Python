from random import randint

# assigning the computer's choices
choices = ["Rock", "Paper", "Scissors"]

# choosing a random word for the computer
computer = choices[randint(0, 2)]

player = False

while not player:
    player = input("Rock, Paper, Scissors.")
    if player == computer:
        print("Tie!")
    elif player.lower() == "rock":
        if computer == "Scissors":
            print(f"You won! {player} beats {computer}")
        else:
            print(f"You lost! {computer} beats {player}")
    elif player.lower() == "Paper":
        if computer == "Rock":
            print(f"You won! {player} beats {computer}")
        else:
            print(f"You lost! {computer} beats {player}")
    elif player.lower() == "Scissors":
        if computer == "Paper":
            if computer == "Rock":
                print(f"You won! {player} beats {computer}")
            else:
                print(f"You lost! {computer} beats {player}")
    else:
        print("Not a valid play.")

    player = False
    computer = choices[randint(0, 2)]
