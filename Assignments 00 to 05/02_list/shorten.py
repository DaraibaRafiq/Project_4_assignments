MAX_LENGTH = 3  # The maximum allowed length of the list

# This function shortens the list if it's too long
def shorten_list(lst):
    while len(lst) > MAX_LENGTH:  # While the list has more than 3 items
        removed_item = lst.pop()  # Remove the last item from the list
        print("Removed:", removed_item)  # Show which item was removed


# This function gets a list of items from the user
def get_user_list():
    user_list = []  # Create an empty list

    while True:
        item = input("Enter an item (or press enter to stop): ")
        if item == "":  # Stop when the user presses enter without typing anything
            break
        user_list.append(item)  # Add the item to the list

    return user_list  # Return the final list


# Let's put everything together
def run_program():
    my_list = get_user_list()  # Get the list from the user
    shorten_list(my_list)  # Shorten the list if needed
    print("Final list:", my_list)  # Display the final list


# Run the program
run_program()
