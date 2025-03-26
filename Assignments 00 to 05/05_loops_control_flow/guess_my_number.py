import random
def main():
    secret_number=random.randint(1,100)
    try:
     while True:
        user_input=int(input("Enter a number guess : "))
        if user_input==secret_number:
            print("You guessed it right!")
            break
        elif user_input>secret_number:
            print("Too high!")
        elif user_input<secret_number:
            print("Too low!")   
    except ValueError:
        print("Invalid input. Please enter a number.")
main()