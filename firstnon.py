#this program is used for looping through a string 

jula = str(input("Enter a string: "))
for char in jula:
    print(char)
       
    if jula.count(char) == 1:
        print(" The Non Repeated character is :",char)
        break
    