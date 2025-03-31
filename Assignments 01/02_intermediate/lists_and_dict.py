def list_practice():
    # Create a list of fruits
    fruits = ["apple", "banana", "orange", "grape", "pineapple"]

    # Print the number of items in the list
    print("Number of fruits:", len(fruits))

    # Add 'mango' to the list
    fruits.append("mango")

    # Print the updated list
    print("Updated list:", fruits)

def index_game():
    # Create a list of items
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    
    print("\nYour list:", items)

    # Ask user for an index
    try:
        index = int(input("Enter an index (0-4): "))

        # Check if index is valid
        if 0 <= index < len(items):
            print("Item at index", index, ":", items[index])
        else:
            print("Invalid index! Please enter a number between 0 and 4.")
    
    except ValueError:
        print("Please enter a valid number!")

# Run both functions
list_practice()
index_game()
