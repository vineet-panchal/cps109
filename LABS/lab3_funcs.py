import math

# --------------------------------------------------------------
# 1) TMU Letter Grade Converter
# --------------------------------------------------------------
def lettergrade(pct):
    
    '''
    A classic problem, but classics are classic for a reason.
    
    Assume that parameter 'pct' is an integer representing
    a percentage grade.
    
    Return the letter grade (as a string) corresponding to this 
    percentage. To keep things simple, we won't worry about +/-. 

    80 to 100 = A
    70 to 79  = B
    60 to 69  = C
    50 to 59  = D
    0  to 49  = F

    If the value of pct is outside this range, return None.

    '''
    
    if (pct >= 0 and pct <= 49):
        return "F"
    elif (pct >= 50 and pct <= 59):
        return "D"
    elif (pct >= 60 and pct <= 69):
        return "C"
    elif (pct >= 70 and pct <= 79):
        return "B"
    elif (pct >= 80 and pct <= 100):
        return "A"
    else:
        return None

    # pass # replace 'pass' with a return statement.
# if __name__ == "__main__":
    
#     for i in range(-10, 110):
#         print(lettergrade(i))
#         i += 5

# --------------------------------------------------------------
# 2) Duplicate Sequence Elements
# --------------------------------------------------------------
def duplicates(items):

    '''
    Assume that parameter 'items' is a sequence. Return a 
    string according to the following criteria:
    
    If items does not contain exactly three elements,
    return the string 'invalid input'
    
    if items contains three elements, and they're all the same,
    return the string 'three-of-a-kind'
    
    if items contains three elements, and two are the same,
    return the string 'two-of-a-kind'
    
    if items contains three elements, and none are the same,
    return the string 'one-of-a-kind'
        
    FOOD FOR THOUGHT:    
    This function should work on all three 
    sequence types we've seen - strings, lists, and tuples. 
    Do you have to do anything different for the different types, 
    or can your code be exactly the same regardless of the 
    sequence type? This is a VERY powerful notion in computer 
    science that you will explore further in future courses. 

    '''

    # pass # replace 'pass' with a return statement.
    
    # if (len(items) != 3):
    #     return "invalid input"
    # else:
    #     for i in range(len(items)):
    #         for j in range(len(items)):
    #             if (items[j]):
    
    if (len(items) != 3):
        return "invalid input"
    else:
        if (items[0] == items[2] and items[0] == items[1]):
            return "three-of-a-kind"
        elif (items[0] == items[1] and items[1] != items[2]):
            return "two-of-a-kind"
        elif (items[1] == items[2] and items[1] != items[0]):
            return "two-of-a-kind"
        elif (items[0] == items[2] and items[2] != items[1]):
            return "two-of-a-kind"
        else:
            return "one-of-a-kind"
        
# array test 
# arr = [4, 4, 4, 5]
# print(duplicates(arr))

# string test
# string = "4544"
# print(duplicates(string))



# --------------------------------------------------------------
# 3) Inversions of Three
# --------------------------------------------------------------
def inversions(items):

    '''
    Like the previous question, you may assume 'items' 
    is a sequence. Also like the previous question, it should
    not matter if items is a string, list, or tuple.
    
    If items does not contain exactly three elements,
    return the integer -1.
    
    If items contains exactly three values, return the number
    of inversions in the sequence.
    
    In a sequence, an 'inversion' is a pair of elements that 
    are out of order with respect to the sorted sequence.
    We will consider 'sorted' to mean ascending order.
    
    For example:
    
    The list [1, 2, 3] contains zero inversions, because 
    the list is in ascending order.
    
    The list [2, 1, 3] contains one inversion, because the
    2 and the 1 are out of order with respect to each other.
    
    The list [3, 2, 1] contains THREE inversions. The 3 is 
    out of order with respect to both 2 and 1 (two inversions)
    and the 2 is out of order with respect to 1 (one more inversion)
    for a total of three inversions. 
    
    For an added challenge, try solving this problem using as few
    comparisons (<, >, <=, >=) as possible.
    
    FOOD FOR THOUGHT:    
    Once you've solved this problem, think about how your code 
    would have to change if there were four elements, five elements, 
    six elements, etc. Notice how the complexity grows. 
    How many more comparisons would you need for four elements? 
    Five elements? 100 elements? 
    What is the relationship between the number of comparisons
    and the number of elements in the sequence? This is another 
    supremely important notion that we'll explore further towards
    the end of the course, and in future courses.
    
    '''
    
    inversions = 0

    if (len(items) == 3):
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if (items[i] > items[j]):
                    inversions += 1
        
        return inversions
    
    else: 
        return -1

    # pass # replace 'pass' with a return statement.    

# test
# print(inversions("231"))

# --------------------------------------------------------------
# 4) Increasing, Strictly or Otherwise?
# --------------------------------------------------------------   
def increasing(items, strict):   
    
    '''
    Once more, assume items is a sequence. The second parameter,
    'strict', is boolean (True or False)
    
    If items does not contain exactly three elements,
    return the string 'invalid input'
    
    If 'strict' is something other than True or False, 
    return the string 'invalid input'
    
    If the sequence contains three elements, we now want to
    determine if it is ascending. However, there's a twist - we
    will distinguish between ascending, and strictly ascending.
    
    If a sequence is ascending, every element is greater than 
    or equal to the one that came before it.
    
    If a sequence is strictly ascending, every element is 
    strictly greater than the one that came before it.
    
    If parameter 'strict' is True, you should test for
    strictly ascending. If it is False, check for simple
    ascending.
    
    In either case, return True if the 'items' is ascending,
    strict or otherwise, and False if not. 
    '''
    
    
    # pass # replace 'pass' with a return statement.



    if (len(items) != 3 or strict not in (True, False)):
        return "invalid input"
    else:
        for i in range(1, 3):
            if strict:
                if items[i] <= items[i - 1]:
                    return False
            else:
                if items[i] < items[i - 1]:
                    return False
        return True

    # count = 0
    # count2 = 0
    
    # if (len(items) != 3):
    #     return "invalid input"
    # elif (strict != True and strict != False):
    #     return "invalid input"
    # elif (strict == True):
    #     for i in range(len(items)):
    #         for j in range(i + 1, len(items)):
    #             if (items[j] - items[i] == 1):
    #                 count += 1
    #     if (count == len(items) - 1):
    #         # return True
    #         return True
    #     else:
    #         # return False
    #         return False
    # elif (strict == False):
    #     for p in range(len(items)):
    #         for v in range(p + 1, len(items)):
    #             if (items[v] - items[p] == 1):
    #                 count += 1
    #             elif (items[v] - items[p] > 0):
    #                 count2 += 1
    #     if (count == len(items) - 1):
    #         # return False
    #         return False
    #     elif (count2 > 0):
    #         return True
                    

# --------------------------------------------------------------
# 5) Python as a Calculator 
# --------------------------------------------------------------      
def calculator(op1, op2, operator):     
    
    '''
    This function accepts three arguments:
    op1, op2: assume both of these are integers
    operator: assume this argument is a string.
    
    This function should return the arithmetic result of the
    expression <op1> <operator> <op2>
    
    For example, if 'operator' is the string '+', return
    op1 + op2.
    
    Your function should recognize the following five operators:
    '+', '-', '*', '/', and '**'. 
    
    Additionally, your function should not perform division by
    zero. Implement the necessary check to ensure this doesn't 
    happen.
    
    If the operator is not one of the five above, or there
    would be a division by zero, return None.
    '''
    
    # pass # replace 'pass' with a return statement.
    
    if (operator == "+"):
        return op1 + op2
    elif (operator == "-"):
        return op1 - op2
    elif (operator == "*"):
        return op1 * op2
    elif (operator == "/"):
        if (op2 == 0):
            return None
        else: 
            return op1 / op2
    elif (operator == "**"):
        return math.pow(op1, op2)

# test
# print(str(calculator(3, 0, "/")))