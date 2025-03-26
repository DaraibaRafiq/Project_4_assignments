import random  # Importing the random module to generate random numbers

# Setting the chance of stopping the counting
DONE_LIKELIHOOD = 0.5  # 50% chance of stopping at each step

def done():
    """ Returns True if we should stop counting, otherwise returns False. """
    if random.random() < DONE_LIKELIHOOD:  # Randomly decide if we should stop
        return True
    return False

def chaotic_counting():
    """ Counts from 1 to 10, but can randomly stop before reaching 10. """
    for i in range(10):  # Loop 10 times to count from 1 to 10
        current_number = i + 1  # Making sure counting starts from 1 instead of 0

        if done():  # Check if the program wants to stop early
            return  # Stop the function and go back to the main function

        print(current_number)  # Print the current number

def main():
    print("I'm going to count from 1 to 10, but I might randomly stop before reaching 10.")
    chaotic_counting()  # Call the counting function
    print("I'm done!")  # Let the user know the program has finished

main()
