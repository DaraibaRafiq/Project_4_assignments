def read_phonebook():
    phonebook = {}  

    while True:
        name = input("Enter name: ")
        if name == "":
            break  

        number = input("Enter number: ")
        phonebook[name] = number  

    return phonebook  


def print_phonebook(phonebook):
    """
    Yeh function phonebook ke saare names aur numbers ko print karta hai.
    """
    print("\nPhonebook Entries:")
    for name, number in phonebook.items():  # Har name, number ko dikhata hai
        print(f"{name} -> {number}")


def lookup_number(phonebook):
    """
    Yeh function user se naam poochta hai 
    aur uske number ko dhoondh kar print karta hai.
    """
    while True:
        name = input("\nEnter name to lookup (or press Enter to stop): ")
        if name == "":  # Agar user ne sirf enter press kar diya
            break  # Loop ko stop kar do

        if name in phonebook:  # Agar naam dictionary mein hai
            print(f"{name}'s Number: {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")  # Agar naam nahi mila


# Ye sab kuch combine karne ke liye
def main():
    phonebook = read_phonebook()
    print_phonebook(phonebook)    
    lookup_number(phonebook)      
main()
