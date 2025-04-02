import random
choices = ["rock", "paper", "scissor"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissor.")
        continue

    computer_choice = random.choice(choices)  
    print(f"Computer choice: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("Match Draw! Both chose the same.")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You Win!")
    else:
        print("Computer Wins!")

    # Ask the user to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":  # Fixed `=!` to `!=`
        print("Thanks for playing!")
        break
