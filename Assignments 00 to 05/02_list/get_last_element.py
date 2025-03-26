def get_last_element(lst):
    print("The last element is:", lst[-1])

def get_lst():
    lst = []
    while True:
        element = input("Enter a list element (Or press enter to stop): ")
        if element == "":  
            break
        lst.append(element)  
    return lst
user_list = get_lst()  
get_last_element(user_list)  
