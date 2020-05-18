import math

def factorial(a):
    '''(number) -> number

    Calculates and returns the factorial of a.

    >>> factorial(5)
    120

    >>> factorial(0)
    1

    >>> factorial(-1)
    Does not exist
    '''

    if a == 0:
        return 1

    if a < 0:
        print('Invalid input, terminating program')
        quit()
    
    return a * factorial(a-1)
    
def calculate_sin(x, k):
    '''(number, number) 

    Prints the value of Taylor series of x upto k terms.

    >>> calculate_sin(5,10)
    0.08715574274765817
    
    >>> calculate_sin(-10,50)
    -0.17364817766693033
    '''
    x = math.radians(x)
    sum = 0
    for i in range(k):
        t = (2 * i) + 1
        sum += ((-1)**i) * (x**t) / factorial(t)
    print(sum)
