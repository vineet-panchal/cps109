'''
Author: Vineet Panchal
Date: November 25, 2023
Course: CPS 109, Section #072
Assignment: Lab 1

Title: Bank Simulator

Problem: To develop an efficient system for different bank transactions.

Description:
This program shall be a simulation of a bank and be able to perform different bank tasks.
Users will be exposed to an organized and efficient system that allows for easy accessibility to their bank accounts.
The user will have the option to choose from several options such as deposit, withdraw, checking balance, creating account, transferring funds, and getting a list of accounts.
The user will have 9 options to choose from which can be accessed by simply entering an integer from 0-8. Each integer represents a different task for the program to perform.
There is an input text that shows a listing of many different accounts that are already part of the system. The program will read this file and incorporate those accounts along with the program.
Option 1 will allow the user to create a new account ny entering first and last name. It will give the user a random generated account number and set the balance to 0.
Option 2 will allow the user to view the balance of any given account number.
Option 3 will allow the user to deposit money into any given account number.
Option 4 will allow the user to withdraw money from any given account number.
Option 5 will allow the user to transfer money from one account to another.
Option 6 will allow the user to see all the information of a given account.
Option 7 will create a new file and will write all the information for all the accounts by ordering them by account number.
Option 8 will create a new file and will write all the information for all the accounts by ordering them by first names.
Option 0 will allow the user to exit the program.
The program will introduce a new approach to banking and solves the problem to develop an efficient system for different bank transactions.

Functionality and Shall Statements:
1. The program shall have a main menu that allows the user to select a bank task.
2. The program shall include a method that reads the file accounts_data.txt.
3. The program shall create a new account, given the required information by the user.
4. The program shall print the balance of the parallel account number given by the user.
5. The program shall deposit money into the account given by the user.
6. The program shall withdraw money from the account given by the user.
7. The program shall transfer funds from one account to another, given the required information by the user.
8. The program shall list all the accounts ordered numerically and print the information on a file created by the program called cps109_a1_output.txt.
9. The program shall list all the accounts ordered alphabetically and print the information on a file created by the program called cps109_a1_output.txt.
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
    firstName = str(input("Enter your first name: ")) # asking for first name
    lastName = str(input("Enter your last name: ")) # asking for last name
    while True:
    # create a new random account and make sure it isn't the same as the other numbers
        acctNum = random.randint(100000, 999999) # range for account numbers
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
    acct = int(input("Enter account number to check balance for: "))
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
    acct = int(input("Enter account number to deposit to: "))
    if acct in acctList: # if account is found
        index = acctList.index(acct)
        print("The current balance is: $" + str(balList[index]))
        # print balance amount to let the user know
        amount = float(input("How much would you like to deposit? $"))
        print("Deposit Successful.")
        print("")
        new_bal = balList[index] + amount # Deposit: add amount to account paralleled balance
        balList[index] = new_bal
        print("Your new balance is: $" + str(new_bal)) # print new balance
        print("")
    else: # account not found
        print("Account not found.")
        print("")

def withdraw(acctList, balList):
    # Withdraw method
    # Definition: Takes two parameters: list of accounts and list of balances.
    # Prompts the user to enter an amount to be withdrawn from their account.
    # Subtracts this amount from the current balance of the account they entered.
    acct = int(input("Enter account number to withdraw from: "))
    if acct in acctList: # if found account
        index = acctList.index(acct)
        print("The current balance is: $" + str(balList[index]))
        correctAmt = False # to check if user will input the right amt to withdraw 
        while not correctAmt:
            amount = float(input("Enter amount you want to withdraw: $"))
            if amount > balList[index] or amount < 0: # if amt is not in the range of (0-amt in acct)
                print("Insufficient funds! Please try again.")
                print("")
                correctAmt = False # incorrect input
            else: # correct input
                print("Withdrawal successful.")
                print("")
                new_bal = balList[index] - amount # Withdraw: take out the amt requested by the user
                balList[index] = new_bal
                print("Your new balance is: $" + str(new_bal)) # print new balance
                print("")
                break
    else: # account not found
        print("Account not found.")
        print("")

def transfer(acctList, balList):
    acctOne = int(input("Enter the first account (Transferred From): ")) # asking for first account
    if acctOne in acctList: # if first account is found
        indexOne = acctList.index(acctOne) # setting up index for first account
        acctTwo = int(input("Enter the second account (Transferred To): ")) # asking for second account
        if acctTwo in acctList: # if second account found
            indexTwo = acctList.index(acctTwo) # setting up index for second account
            print("The current balance of the first account is: $" + str(balList[indexOne]))
            print("The current balance of the second account is: $" + str(balList[indexTwo]))
            # printing balances of both accounts
            correctAmt = False # for correct amt to transfer (0-amt in first acct)
            while not correctAmt:
                amount = float(input("Enter the amount you want to transfer: $"))
                if amount > balList[indexOne]: # amt not in range 
                    print("Insufficient funds! Please try again.")
                    print("")
                    correctAmt = False # incorrect input
                else: # correct input
                    balList[indexTwo] = balList[indexTwo] + amount # add the transferring amt to second account
                    balList[indexOne] = balList[indexOne] - amount # subtract the transferring amt from first account
                    print("The new balance for #" + str(acctList[indexTwo]) + " is: $" + str(balList[indexTwo])) # print new balance of second account
                    print("Transferred Successfully.")
                    print("")
                    break
        else: # second account not found
            print("Account not found.")
            print("")
    else: # first account not found
        print("Account not found.")
        print("")

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
    if left < right:
        pos = partition(acctList, left, right, firstList, lastList, balList)
        # setting up the position for the partition
        numericSort(acctList, left, pos - 1, firstList, lastList, balList)
        numericSort(acctList, pos + 1, right, firstList, lastList, balList)
        # recursion, add to position for left, and subtract from position for right
    
    writeFile(firstList, lastList, acctList, balList, "cps109_a1_output.txt")
    # calling method to write the information and create a file

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
            # the swap method to swap main list (the accounts list)
            # swap rest of the parallel lists side by side
            arr[i], arr[j] = arr[j], arr[i]
            firstList[i], firstList[j] = firstList[j], firstList[i]
            lastList[i], lastList[j] = lastList[j], lastList[i]
            balList[i], balList[j] = balList[j], balList[i]
    if arr[i] > pivot:
        # the swap method to swap main list (the accounts list)
        # swap rest of the parallel lists side by side
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
    pivot = arr[len(arr) // 2] # define pivot variable (right)
    
    # USE OF FOR LOOP ITERATION to check pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # left and right pointers condition statements, middle if it is equal
    
    return alphabetSort(left) + middle + alphabetSort(right)
    # recursion, created new list and sort, and repeat

def writeFile(firstNames, lastNames, accounts, balances, filename):
    # Write the data to a file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    # I had trouble putting the created file in the same directory as my folder
    # I researched online and found a viable solution
    # CREDIT: https://www.tutorialspoint.com/How-to-open-a-file-in-the-same-directory-as-a-Python-script
    with open(filepath, "w+") as file: # open file with "w+" to read and write
        for i in range(len(firstNames)):
            file.write(f"Account Holder: {firstNames[i]} {lastNames[i]}\n")
            file.write(f"Account Number: {accounts[i]}\n")
            file.write(f"Balance: $ {balances[i]}\n")
            file.write("\n")
        # write information in a proper, easy-to-read format
    file.close() # close file
def main():
    filepath = '/Users/vineetpanchal/Desktop/TMU/YEAR-1/FALL-2023/CPS109/Assignment/draft-4/accounts_data.txt'
    
    file = open(filepath, 'r') # opening file to read
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
    
    file.close() # close file
    
    # USE OF WHILE LOOP FOR GENERAL ITERATION:
    while True:
    # main while loop
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
        
        if num < 0 or num > 8: # range of menu (0-8)
            print("Invalid entry. . . Integer entered must be in range (0-8).")
            print("")
        elif num == 1: # create new account
            createNewAcct(firstNames, lastNames, acctNumbers, balNumbers)
        elif num == 2: # get balance
            getBal(acctNumbers, balNumbers)
        elif num == 3: # deposit
            deposit(acctNumbers, balNumbers)
        elif num == 4: # withdraw
            withdraw(acctNumbers, balNumbers)
        elif num == 5: # transfer
            transfer(acctNumbers, balNumbers)
        elif num == 6: # print info
            printInfo(firstNames, lastNames, acctNumbers, balNumbers)
        elif num == 7: # numerically order
            numericSort(acctNumbers, 0, len(acctNumbers) - 1, firstNames, lastNames, balNumbers)
            # call quick sort function with acctNumbers being the main array to sort
            # left being the start of the list and right being the end of the list
        elif num == 8: # alphabetically order
            zipList = list(zip(firstNames, lastNames, acctNumbers, balNumbers))
            # make a list of tuples, each tuple is a string from firstNames and parallel to the accounts list
            sortedZipList = alphabetSort(zipList)
            # sort the list of tuples using the second implementation of the quicksort algorithm
            sortedFirstNames, sortedLastNames, sortedAcctNumbers, sortedBalNumbers = zip(*sortedZipList)
            # split the zip file of sorted list of tuples, to each parallel list
            writeFile(sortedFirstNames, sortedLastNames, sortedAcctNumbers, sortedBalNumbers, "cps109_a1_output.txt")
            # calling method to write the information and create a file
            for i in range(len(acctNumbers)):
                print("Account Holder: " + firstNames[i] + " " + lastNames[i])
                print("Account Number: " + str(acctNumbers[i]))
                print("Balance: $" + str(balNumbers[i]))
                print("\n")
        else: # 0 entered 
            print("Program exiting. . . ")
            print("")
            break # breaking main loop

if __name__ == "__main__":
    main()
    # calling main function