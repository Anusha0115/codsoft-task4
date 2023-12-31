
import random

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ")
    return user_choice.lower()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    if user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    if user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break


