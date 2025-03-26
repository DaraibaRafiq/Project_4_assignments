numbers=[1,2,3,4,5,6,7,8,9,10]
def main():
    total=0
    for i in numbers:
        total+=i
        return total
response=sum(numbers)
print(response)
main()