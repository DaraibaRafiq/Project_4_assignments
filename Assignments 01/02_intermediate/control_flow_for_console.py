import random
NUM_ROUNDS = 5  # Total rounds
def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0  
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is {your_num}")
        while True:
            choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if choice in ["higher", "lower"]:
                break
            print("Invalid input! Please enter 'higher' or 'lower'.")

        # Check if guess is correct
        if (choice == "higher" and your_num > computer_num) or (choice == "lower" and your_num < computer_num):
            print("You were right! 🎉")
            score += 1  
        else:
            print("Aww, that's incorrect. 😞")

        print(f"The computer's number was {computer_num}")
        print(f"Your score is now {score}\n")
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly! 🌟")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well! 👍")
    else:
        print("Better luck next time! 😢")
main()
