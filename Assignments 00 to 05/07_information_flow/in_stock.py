def num_in_stock(fruit):
    stock = {
        "apple": 2,
        "durian": 4,
        "pear": 1000
    }
    return stock.get(fruit, 0)

def main():
    fruit = input("Enter a fruit: ") 
    stock = num_in_stock(fruit)  
    
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")
main()
