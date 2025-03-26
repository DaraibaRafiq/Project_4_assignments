def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    
    total_cost = 0

    for fruit in fruits:
        price = fruits[fruit]
        quantity = int(input(f"How many ({fruit}) do you want to buy?: "))
        total_cost += price * quantity

    print(f"Your total is ${total_cost}")

main()
