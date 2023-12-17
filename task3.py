import random

def get_user_choice():
    """Get user's choice for Rock, Paper, or Scissors."""
    while True:
        user_choice = input("1: Rock \n2: Paper \n3: Scissors: \nEnter your choice : ")
        if user_choice in ["1", "2", "3"]:
            choices = ["Rock", "Paper", "Scissors"]
            return choices[int(user_choice) - 1]
        else:
            print("Invalid choice. Please choose 1 for Rock, 2 for Paper, or 3 for Scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "Congratulations! You win!"
    else:
        return "Computer wins. Better luck next time!"

def play_game():
    """Play the Rock, Paper, Scissors game."""
    print("Welcome to the Rock, Paper, Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\nResult: {result}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing. Goodbye!")
            break

# Start the game
play_game()
