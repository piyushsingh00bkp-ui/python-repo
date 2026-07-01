og = int (input("Enter a number :"))
is_prime = True
if og > 1:
      for i in range(2, og):
          if( og %i)==0:
            print(og, "isnotprime number")
            break
          else:
            print(og, "is a prime number")
            break 
                