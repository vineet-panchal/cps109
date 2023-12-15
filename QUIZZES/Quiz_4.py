x = int(input("Enter an integer:"))
print("")

if (x < 1):
    print("N must be greater than 1")
elif (x > 100):
    print("Too much work, no thanks")
else:    
    for i in range(1, x + 1):
        if (i % 3 == 0 and i % 5 == 0):
            print ("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print (i)