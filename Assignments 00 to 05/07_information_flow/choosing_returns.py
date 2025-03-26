def is_adult(age):
    if age >= 18:
        print("Person is an adult.") 
        return True  
    else:
        print("Person is NOT an adult.")  
        return False  

def main():
    age = int(input("How old is this person?: "))  
    result = is_adult(age)  
    print(result) 
main()
