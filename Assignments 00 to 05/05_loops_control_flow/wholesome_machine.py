AFFIRMATION = "I am capable of doing anything I put my mind to."  # The correct sentence

def main():
    while True: 
        print("Please type the following affirmation: " + AFFIRMATION)
        user_input = input("enter your affirmation: ")  
        if user_input == AFFIRMATION:
            print("That's right! :)")
            break 
        else:
            print("That was not the affirmation. Try again.")
main()
