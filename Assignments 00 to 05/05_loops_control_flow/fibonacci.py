MAX_VALUE = 10000  # The maximum value to stop the sequence

def main():
    first = 0    # Starting with the first number of the sequence
    second = 1   # Starting with the second number of the sequence
    
    while first <= MAX_VALUE:
        print(first)  # Print the current number
        
        # Calculate the next number in the sequence
        next_number = first + second
        
        # Move to the next numbers
        first = second
        second = next_number
main()

