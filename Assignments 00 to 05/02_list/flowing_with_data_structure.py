def add_three_copies (list, message):
    for i in range(3):
        list.append(message)

def main():
    message=(input("Enter a message to copy : "))
    list=[]
    print("Original list : ",list)
    add_three_copies (list, message)
    print("New list : ",list)
main()