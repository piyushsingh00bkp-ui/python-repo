age = int (input("Enter your age: "))
day =str(input("Enter the day of the week: "))
price = 12 if (age>=18) else 8
if (age<18 and day == "wednesday"):
    price = price-2
    print("You are a child and it is wednesday and the price would be ", price)
elif (age<18 ):
    print("You are a child and it is not wednesday and the price would be ", price)
elif (age>=18 and day == "wednesday"):
    price = price-2
    print("You are an adult and it is wednesday and the price would be ", price)
else:
    print("You are an adult and it is not wednesday and the price would be ", price)
    