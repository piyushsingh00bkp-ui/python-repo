password =  (input("Enter your password: "))
length = len(str(password))
if(length<6):
    print("Password is too short")
elif(length>6 and length<10): 
    print("Password is acceptable")
elif(length>10):
    print("Password is too long") 
else:
    print("Password is not acceptable")  

