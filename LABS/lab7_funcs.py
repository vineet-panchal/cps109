'''
No description needed at this point. Fill in the functions below
according to the description provided. 

These functions must be solved RECURSIVELY. If your solution does
not use recursion, you risk receiving a zero on the lab submission.

'''

# --------------------------------------------------------------
# 1) Count occurrences
# --------------------------------------------------------------

def count(items, target):

    '''
    This function emulates the list method 'count'. Assume items
    is a list, and target is some object. Return the number of
    times that target appears in items.
    
    YOU MUST USE RECURSION!    
    
    '''
    
    if not items:
        return 0
    if items[0] == target:
        return 1 + count(items[1:], target)
    return count(items[1:], target)
    
if __name__ == "__main__":
    print(count([1, "apple", 2, "banana", 2, "cherry", 2], 2))
    
# --------------------------------------------------------------
# 2) Sum of integers
# --------------------------------------------------------------

def integer_sum(items):

    '''
    This function calculates and returns the sum of the integer
    values in the list 'items'.
    
    Be careful - items may contain things other than integers!
    
    For example, if the input is [ 1, 3, 'hello', 5.66 ], you 
    should return 4 (1 + 3).
    
    Hint: You can check if an object is an integer by performing 
    the following comparison: type(obj) == int
    
    YOU MUST USE RECURSION!    
    
    '''
    if not items:
        return 0
    if type(items[0]) == int:
        return items[0] + integer_sum(items[1:])
    return integer_sum(items[1:])

if __name__ == "__main__":
    print(integer_sum([1, 3, 'hello', 5.66]))
    

# --------------------------------------------------------------
# 3) Exponentiation
# --------------------------------------------------------------

def pow_rec(base, exponent):

    '''
    Assume that base and exponent are integers >= 0.
    
    Calculate and return base to the power of exponent using 
    repeated multiplications.
    
    YOU MUST USE RECURSION!

    '''
    
    if exponent == 0:
        return 1
    else:
        return base * pow_rec(base, exponent - 1)

if __name__ == "__main__":
    print(pow_rec(2, 4))


    
# --------------------------------------------------------------
# 4) Palindrome checker
# --------------------------------------------------------------

def is_palindrome(text):

    '''
    A recursion classic.
    
    Assume that 'text' is a string. Return True if text is a 
    palindrome, and False otherwise. 
    
    A string is a palindrome if it reads the same forwards and
    backwards. For example, 'racecar' is a palindrome.
    
    YOU MUST USE RECURSION!

    '''
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])
    
if __name__ == "__main__":
    print(is_palindrome("racecar"))

# --------------------------------------------------------------
# 5) Nested list reverser
# --------------------------------------------------------------

def nested_reverse(items):

    '''
    Assume that items is a list, that may contain nested lists
    as elements. This function will perform a reverse operation,
    but with a twist - nested sublists must be reveresed as well.
    
    For example, if the input is [ 1, 2, [5, 4, 3, [9, 0], 3 ] ]
    then you should return [ [ 3, [0, 9], 3, 4, 5], 2, 1 ]

    Hint: You can check if an object is a list by performing the 
    following comparison: type(obj) == list
    
    YOU MUST USE RECURSION!

    '''
    
    arr = []
    for i in items:
        if type(i) == list:
            arr += [nested_reverse(i)]
        else:
            arr += [i]
    return arr[::-1]
    # Reverse the array to get correct order of reversal    

if __name__ == "__main__":
    print(nested_reverse([1, 2, [5, 4, 3, [9, 0], 3]]))

