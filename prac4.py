

while id not in range(1, 11):
    id = int(input("Enter a number between 1 and 10: "))
    print("You entered a wrong number. Please try again.")
    if (id in range(1, 11)):
        print("You entered a correct number.")