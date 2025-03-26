def count_even(numbers):
    """ Counts how many even numbers are in the list. """
    count = 0  
    for num in numbers:  
        if num % 2 == 0:  
            count += 1  
    print("Number of even numbers:", count)  

def get_numbers():
    """ Takes integers from the user and returns them as a list. """
    numbers = [] 
    while True:
        user_input = input("Enter an integer or press enter to stop: ")  
        if user_input == "":  
            break  
        numbers.append(int(user_input)) 
    return numbers  
def main():
    numbers = get_numbers()  
    count_even(numbers)  
main()
