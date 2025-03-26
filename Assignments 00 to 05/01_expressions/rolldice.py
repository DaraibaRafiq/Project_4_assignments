import random
one_side=6
def main():
    die1=random.randint(1,one_side)
    die2=random.randint(1,one_side)
    total=int=die1+die2
    print(f"first die : {die1}")
    print(f"second die : {die2}")
    print(f"total of two dies {total}")
main()