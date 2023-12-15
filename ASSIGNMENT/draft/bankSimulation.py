'''
Author: Vineet Panchal
Date: November 25, 2023
Course: CPS 109, Section #072
Assignment: Lab 1

Title: Bank Simulator
Description: This program shall be a simulation of a bank and be able to perform different bank tasks.
It shall include a method that reads the file accounts_data.txt and create an Accoun


'''

import csv
import random
import os
# importing necessary libraries

def createNewAcct(firstList, lastList, acctList, balList):
    # Create New Account method
    # Definition: Takes four parameters: list of first names, list of last names, list of accounts, and list of balances
    # Creates a new account by asking user for first and last name, sets balance to 0 and gives a random account number.
    # Appends each of the values to their corresponding lists.
    print("Create New Account")
    firstName = str(input("Enter your first name: ")) # asking for first name
    lastName = str(input("Enter your last name: ")) # asking for last name
    while True:
    # create a new random account and make sure it isn't the same as the other numbers
        acctNum = random.randint(100000, 999999)
        if acctNum not in acctList:
            break
    balance = 0.0 # balance will be set to 0
    firstList.append(firstName)
    lastList.append(lastName)
    acctList.append(acctNum)
    balList.append(balance)
    # create new account by appending to each list

def getBal(acctList, balList):
    # Get Balance method
    # Definition: Takes two parameters: list of accounts, and list of balances.
    # Finds the account given by the user in the list of accounts.
    # Returns the balance associated with a given account number.
    print("Get Balance")
    acct = int(input("Enter account number to check balance for: "))
    print(acct)
    print(type(acct))
    if acct in acctList: # if account is found
        index = acctList.index(acct)
        print("The balance is: $" + str(balList[index]))
        print("")
        # print balance of the account from the parallel list
    else:
        print("Account not found.")
        print("")

def deposit(acctList, balList):
    # Deposit method
    # Definition: Takes two parameters: list of accounts and list of balances.
    # Prompts the user to enter an amount to be deposited into their account.
    # Adds this amount to the current balance of the account they entered.
    print("Deposit")
    acct = int(input("Enter account number to deposit to: "))
    print(acct)
    if acct in acctList: # if account is found
        index = acctList.index(acct)
        print("The current balance is: $" + str(balList[index]))
        # print balance amount to let the user know
        amount = float(input("How much would you like to deposit? $"))
        print("Deposit Successful.")
        print("")
        new_bal = balList[index] + amount
        balList[index] = new_bal
        print("Your new balance is: $" + str(new_bal))
        print("")
    else:
        print("Account not found.")
        print("")

def withdraw(acctList, balList):
    # Withdraw method
    # Definition: Takes two parameters: list of accounts and list of balances.
    # Prompts the user to enter an amount to be withdrawn from their account.
    # Subtracts this amount from the current balance of the account they entered.
    print("Withdrawal")
    acct = int(input("Enter account number to withdraw from: "))
    if acct in acctList:
        index = acctList.index(acct)
        print("The current balance is: $" + str(balList[index]))
        correctAmt = False
        while not correctAmt:
            amount = float(input("Enter amount you want to withdraw: $"))
            if amount > balList[index] or amount < 0:
                print("Insufficient funds! Please try again.")
                print("")
                correctAmt = False
            else:
                print("Withdrawal successful.")
                print("")
                new_bal = balList[index] - amount
                balList[index] = new_bal
                print("Your new balance is: $" + str(new_bal))
                print("")
                break
    else:
        print("Account not found.")
        print("")

def transfer():
    print("Transfer")

def printInfo(firstList, lastList, acctList, balList):
    # Print Info method
    # Definition: Takes four parameters: list of first names, list of last names, list of accounts, and list of balances
    # Prints the information for a given account number by the user using the parallel index.
    acct = int(input("Enter account number to print info: "))
    if acct in acctList: # if account is found
        index = acctList.index(acct) # get index of the account in list
        firstName = firstList[index]
        lastName = lastList[index]
        # get the parallel items
        print("Account Holder: " + firstName + " " + lastName)
        print("Account Number: " + str(acct))
        print("Balance: $" + str(balList[index]))
        print("") 
        # print info in a proper format       
    else: # else account not found
        print("Account not found.")
        print("")
def numericSort(acctList, left, right, firstList, lastList, balList):
    # Numeric Sort method
    # Definiton: Takes six parameters: list of accounts as main list, left pointer, right pointer, list of first names, list of last names, and list of balances
    # My implementation of the Quick Sort Algorithm, method 1 for numerically sorting
    # Big O Notation: O(n logn)
    # Space Complexity: O(logn)
    print("Numeric Sort")
    if left < right:
        pos = partition(acctList, left, right, firstList, lastList, balList)
        numericSort(acctList, left, pos - 1, firstList, lastList, balList)
        numericSort(acctList, pos + 1, right, firstList, lastList, balList)

def partition(arr, left, right, firstList, lastList, balList):
    i = left # start of the list (left pointer)
    j = right - 1 # end of the list (right pointer)
    pivot = arr[right] # initialize the pivot variable for the end most item
    
    while i < j: # while i is still less than j, i and j get closer and closer
        while i < right and arr[i] < pivot: # while left pointer is less than the end and left item is less than the pivot
            i += 1 
        while j > left and arr[j] >= pivot: # while right pointer is less than the start and right item is less than or equal to pivot
            j -= 1
        if i < j: 
            # the swap method
            arr[i], arr[j] = arr[j], arr[i]
            firstList[i], firstList[j] = firstList[j], firstList[i]
            lastList[i], lastList[j] = lastList[j], lastList[i]
            balList[i], balList[j] = balList[j], balList[i]
    if arr[i] > pivot:
        # the swap method
        arr[i], arr[right] = arr[right], arr[i]
        firstList[i], firstList[right] = firstList[right], firstList[i]
        lastList[i], lastList[right] = lastList[right], lastList[i]
        balList[i], balList[right] = balList[right], balList[i]
    return i

def alphabetSort(arr):
    # Numeric Sort method
    # Definiton: Takes six parameters: list of accounts as main list, left pointer, right pointer, list of first names, list of last names, and list of balances
    # My implementation of the Quick Sort Algorithm, method 2 for alphabetically sorting
    # Big O Notation: O(n logn)
    # Space Complexity: O(logn)
    if len(arr) <= 1:
        return arr
    # USE OF A FOR LOOP FOR SEQUENCE ITERATION (LIST COMPREHENSION):
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return alphabetSort(left) + middle + alphabetSort(right)

def writeFile(firstNames, lastNames, accounts, balances, filename):
    # Write the data to a file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    # I had trouble putting the created file in the same directory as my folder
    # I researched online and found a viable solution
    # CREDIT: https://www.tutorialspoint.com/How-to-open-a-file-in-the-same-directory-as-a-Python-script
    with open(filepath, "w+") as file:
        for i in range(len(firstNames)):
            file.write(f"Account Holder: {firstNames[i]} {lastNames[i]}\n")
            file.write(f"Account Number: {accounts[i]}\n")
            file.write(f"Balance: $ {balances[i]}\n")
            file.write("\n")
    file.close()
def main():
    filepath = '/Users/vineetpanchal/Desktop/TMU/YEAR-1/FALL-2023/CPS109/Assignment/draft-4/accounts_data.txt'
    file = open(filepath, 'r')
    # opening file to read

    reader = csv.reader(file, delimiter=' ')
    # seperating reader per space
    
    firstNames = []
    lastNames = []
    acctNumbers = []
    balNumbers = []
    # initializing parallel lists
    
    for row in reader:
        # USE OF SEQUENCE TYPES AND THEIR OPERATIONS (LISTS):
        firstNames.append(str(row[0]))
        lastNames.append(str(row[1]))
        acctNumbers.append(int(row[2]))
        balNumbers.append(float(row[3]))
        # append each column of a row to corresponding lists
    
    file.close()

    print(firstNames)
    print(lastNames)
    print(acctNumbers)
    print(balNumbers)
    print()
    
    # USE OF WHILE LOOP FOR GENERAL ITERATION:
    while True:
        # main while loop
        # try:
            # PRINT STATEMENTS FOR DISPLAYING OUTPUT:
            print("1 - Create New Account")
            print("2 - Get Account Balance")
            print("3 - Deposit Amount")
            print("4 - Withdraw Account")
            print("5 - Transfer Accounts")
            print("6 - Print Account Info")
            print("7 - Listing Of Accounts (Numerically Ordered)")
            print("8 - Listing Of Accounts (Alphabetically Ordered)")
            print("0 - Exit")
            print("")
            # print menu
            
            num = int(input("Enter a positive integer: "))
            print("")
            
            if num < 0 or num > 8:
                print("Invalid entry. . . Integer entered must be in range (0-8).")
                print("")
            elif num == 1:
                print("Create New Account")
                createNewAcct(firstNames, lastNames, acctNumbers, balNumbers)
                for i in range(len(acctNumbers)):
                    print("Account Holder: " + firstNames[i] + " " + lastNames[i])
                    print("Account Number: " + str(acctNumbers[i]))
                    print("Balance: $" + str(balNumbers[i]))
                    print("\n")
            elif num == 2:
                print("Get Balance")
                getBal(acctNumbers, balNumbers)
            elif num == 3:
                print("Deposit")
                deposit(acctNumbers, balNumbers)
            elif num == 4:
                print("Withdraw")
                withdraw(acctNumbers, balNumbers)
            elif num == 5:
                print("Transfer")
            elif num == 6:
                print("Print Info")
                printInfo(firstNames, lastNames, acctNumbers, balNumbers)
            elif num == 7:
                print("List Numeric")
                numericSort(acctNumbers, 0, len(acctNumbers) - 1, firstNames, lastNames, balNumbers)
                # call quick sort function with acctNumbers being the main array to sort
                # left being the start of the list and right being the end of the list
                for i in range(len(acctNumbers)):
                    print("Account Holder: " + firstNames[i] + " " + lastNames[i])
                    print("Account Number: " + str(acctNumbers[i]))
                    print("Balance: $" + str(balNumbers[i]))
                    print("\n")
            elif num == 8:
                print("List Alphabetic")
                # First, we make a list of tuples where each tuple contains a string from the str_list
                # and its corresponding number from the num_list
                zipList = list(zip(firstNames, lastNames, acctNumbers, balNumbers))
                
                # Now, we sort the list of tuples using the quicksort function
                sortedZipList = alphabetSort(zipList)
                
                # Finally, we split the sorted list of tuples into two separate lists:
                # a list of sorted strings and a list of sorted numbers
                sortedFirstNames, sortedLastNames, sortedAcctNumbers, sortedBalNumbers = zip(*sortedZipList)
                for i in range(len(acctNumbers)):
                    print("Account Holder: " + sortedFirstNames[i] + " " + sortedLastNames[i])
                    print("Account Number: " + str(sortedAcctNumbers[i]))
                    print("Balance: $" + str(sortedBalNumbers[i]))
                    print("\n")

                print(sortedFirstNames)
                print(sortedLastNames)
                print(sortedAcctNumbers)
                print(sortedBalNumbers)
                
                writeFile(sortedFirstNames, sortedLastNames, sortedAcctNumbers, sortedBalNumbers, "test.txt")
                
                # f = open('test.txt', 'w')
                # # filename = '/Users/vineetpanchal/Desktop/TMU/YEAR-1/FALL-2023/CPS109/Assignment/draft-4/new_accounts.txt'

                # # with open('test.txt', 'w.txt') as f:
                # for i in range(len(acctNumbers)):
                #     f.write("Hello")
                #     f.writelines("Account Holder: " + sortedFirstNames[i] + " " + sortedLastNames[i] + "\n")
                #     f.write("Account Number: " + str(sortedAcctNumbers[i]) + "\n")
                #     f.write("Balance: $" + str(sortedBalNumbers[i]) + "\n")
                #     f.write("\n")
                # f.close()
            else:
                print("Program exiting. . . ")
                print("")
                break
        # except Exception as e:
        #     print("Invalid entry. . . Must be an integer.")
        #     print("")


# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# # Assuming we have two lists like these:
# str_list = ['orange', 'apple', 'banana', 'cherry', 'lemon']
# num_list = [2, 3, 1, 4, 5]
# bal_list = [0.5, 32.3, 48.4, 1.2, 1.7]
# str2_list = ['hello', 'world', 'my', 'name', 'Jeff']

# # First, we make a list of tuples where each tuple contains a string from the str_list
# # and its corresponding number from the num_list
# zip_list = list(zip(str_list, num_list, bal_list, str2_list))

# # Now, we sort the list of tuples using the quicksort function
# sorted_zip_list = quicksort(zip_list)

# # Finally, we split the sorted list of tuples into two separate lists:
# # a list of sorted strings and a list of sorted numbers
# sorted_str_list, sorted_num_list, sorted_bal_list, sorted_str2_list = zip(*sorted_zip_list)

# print("Sorted strings:", sorted_str_list)
# print("Sorted numbers:", sorted_num_list)
# print("Sorted Balances:", sorted_bal_list)
# print("Strings 2:", sorted_str2_list)
if __name__ == "__main__":
    main()
    # calling main function