def get_first_element(lst):
    print("The first element is:", lst[0])

def get_lst():
    lst = []
    while True:
        element = input("Enter a list element (Or press enter to stop): ")
        if element == "":  # If the user presses enter without typing, stop the loop
            break
        lst.append(element)  # Add the element to the list
    return lst

# Program starts here
user_list = get_lst()  # Get the list from the user
get_first_element(user_list)  # Print the first element of the list
