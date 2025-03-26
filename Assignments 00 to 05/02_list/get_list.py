def get_user_list():
    user_list = []  

    while True:
        value = input("Enter a value: ")
        if value == "":  
            break
        user_list.append(value)  

    return user_list  
def show_list():
    final_list = get_user_list()  
    print("Here's the list:", final_list)  
show_list()
