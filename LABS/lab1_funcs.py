import math

# --------------------------------------------------------------
# 1) Celsius To Fahrenheit
# --------------------------------------------------------------
def celsius_and_fahrenheit(cel):
    '''
    Question 1:
    Convert from celsius to fahrenheit given celsius.
    '''
    
    fahrenheit = (cel * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
    print(celsius_and_fahrenheit(30))

# --------------------------------------------------------------
# 2) Quadratic Formula
# --------------------------------------------------------------

def finding_roots(a, b, c):
    '''
    Question 2:
    Find the roots using the quadratic formula with given three variables for a, b, c.
    '''
    bottom = 2 * a
    sqr = math.pow(b, 2) - (4)
    root1 = (-b + math.sqrt(sqr)) / bottom
    root2 = (-b - math.sqrt(sqr)) / bottom
    
    print("Root #1 is: " + str(root1))
    print("Root #2 is: " + str(root2)) 
    
if __name__ == "__main__":
    print(finding_roots(4, 5, 3))

# --------------------------------------------------------------
# 3) Triangle Or Not
# --------------------------------------------------------------

def triangle(a, b, c):
    '''
    Question 3:
    Check if the given sides can form a triangle.
    '''
    
    return (a + b > c and a + c > b and b + c > a)

if __name__ == "__main__":
    print(triangle(3, 4, 5))

# --------------------------------------------------------------
# 4) Area Of A Pentagon
# --------------------------------------------------------------

def pentagon_area(length):
    '''
    Question 4:
    Calculate the area of a pentagon given the length of a side
    '''
    area = ((0.25 * (math.sqrt(5 * (5 + (2 * math.sqrt(5)))))) * math.pow(length, 2))
    return area

if __name__ == "__main__":
    print(pentagon_area(5))

# --------------------------------------------------------------
# 5) Fibonacci Number
# --------------------------------------------------------------

def fibonacci(num):
    '''
    Question 5:
    Find the fibonacci number to the given number.
    '''
    
    goldenRatio = (math.sqrt(5) + 1) / 2
    fibonacciNumber = (math.pow((1 + math.sqrt(5)), num)) / (math.pow(2, num) * math.sqrt(5))
    return fibonacciNumber

if __name__ == "__main__":
    print(fibonacci(7))
