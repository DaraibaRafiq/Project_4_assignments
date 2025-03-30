import random
def main():
    numbers = 10
    minimum_number = 1
    maximum_number = 100
    random_numbers = [] 

    i = 0  
    while i < numbers:  
        random_number = random.randint(minimum_number, maximum_number)
        random_numbers += [random_number]  
        i += 1  
    print("Generated Numbers:", random_numbers)
main()
