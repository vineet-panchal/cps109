new_password = str(input("Enter a new password:"))
print("")

second_entry = str(input("Enter the same password again:"))
print("")

test = 0

if (new_password == second_entry):
    print("Passwords match.")
    
    if (len(new_password) >= 8):
        test += 1
        print("more than 8")
    
    if (new_password.isalnum() == True):
        test += 1
        print("numbers")
    
    res = False
    for ele in new_password:
        if ele.isupper():
            res = True
            test += 1
            print("uppercase letters")
            break
    
    # if (character.isalpha()):
    #   if not 
    
    # if (character.lower() == character)
    
    for char in new_password:
        k = char.islower() 
        if k == True:
            test += 1
            
            print("lowercase letters")
            break 

    if(k != 1):
        test += 0
        print("no lowercase letters")
    
    if (test == 4):
        print("Password changed successfully.")
    elif (test != 4): 
        print("Password not complex enough.")
        
else:
    print("Passwords must match.")