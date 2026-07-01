goon = int (input("Enter a number to find the factorial: "))
hul = goon
fact =1 
# for i in range(1, goon + 1):
#     fact = fact * i
# print("The factorial of", goon, "is", fact) 
while goon > 0:
    fact = fact * goon
    goon = goon - 1
print("The factorial of", hul, "is", fact) 