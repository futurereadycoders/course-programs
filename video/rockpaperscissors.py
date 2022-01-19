import random

choices = ["rock", "paper", "scissors"]
print("Hello! Welcome to Rock-Paper-Scissors!")


def main():
    computer_choice = random.choice(choices)
    human_choice = input("What is your choice? ").lower()
    if human_choice not in choices:
        print("Error: invalid choice.")
        exit(1)
    if (
        (human_choice == "rock" and computer_choice == "paper")
        or (human_choice == "paper" and computer_choice == "scissors")
        or (human_choice == "scissors" and computer_choice == "rock")
    ):
        print(f"I won! I chose {computer_choice}.")
    elif human_choice == computer_choice:
        print("It's a tie!")
    else:
        print(f"You won! I chose {computer_choice}.")

    goagain = input("Would you like to play again? ").lower()
    if goagain == "y":
        main()
    print("Thanks for playing!")

main()
