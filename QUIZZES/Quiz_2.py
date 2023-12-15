# CPS109 Quiz #2

x = int(input("Enter an integer: "))
print("")

y = []



for i in range(2, 11):
    if (x % i == 0):
        y.append(i)
        
    else:
        print("")
        

if y:
    print("The factors of " + str(x) + " between 2 and 10 are: ", end='')
    for j in y:
        print(*str(j), end=" ", sep=",")
if not y:
    print("This number has no factors between 2 and 10")
    

