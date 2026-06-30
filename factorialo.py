goon = int (input("Enter a number to find the factorial: "))
fact =1 
for i in range(1, goon + 1):
    fact = fact * i
print("The factorial of", goon, "is", fact) 