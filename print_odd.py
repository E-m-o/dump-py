import math

def print_odd_for(a, b):
    '''
    Takes in two numbers as range and prints out all odd numbers 
    between them, excluding the last number.

    >>> print_odd_for()
    Enter start point: 10
    Enter end point  : 20
    11
    13
    15
    17
    19

    >>> print_odd_for()
    Enter start point: 2 
    Enter end point  : 1
    Invalid inputs

    '''

    if a == None or b == None:
        a = float(input('Enter start point: '))
        b = float(input('Enter end point  : '))

    if b < a:
        print('Invalid input, terminating program...')
        quit()
    
    #converting floats to integers
    a = math.ceil(a)
    b = math.floor(b)

    for num in range(a, b):
        if num % 2 != 0:
            print(num)


def print_odd_while(a , b):
    '''
    Takes in two numbers as range and prints out all odd numbers 
    between them, excluding the last number.

    >>> print_odd_for()
    Enter start point: 10
    Enter end point  : 20
    11
    13
    15
    17
    19

    >>> print_odd_for()
    Enter start point: 2 
    Enter end point  : 1
    Invalid inputs

    '''
    if a == None or b == None:
        a = float(input('Enter start point: '))
        b = float(input('Enter end point  : '))

    if b < a:
        print('Invalid input, terminating program...')
        quit()
    
    #converting floats to integers
    a = math.ceil(a)
    b = math.floor(b)

    num = a
    i = 0
    while i < len(range(a, b)):
        if num % 2 != 0:
            print(num)
        num += 1
        i += 1