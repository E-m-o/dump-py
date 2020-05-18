import math
#need math for converting to radians
#Question 1###################################################################
def am_gm_hm(a, b):
    '''(number, number)

    Find the arithmetic mean, geometric mean and harmonic mean
    of numbers a and b, and print them in that order.
    
    Numbers get converted to float.
    
    >>> am_gm_hm(10,20)
    arithmetic mean = 15.0
    geometric mean = 14.142135623730951
    harmonic mean = 13.333333333333332

    >>> am_gm_hm(-10,20)
    arithmetic mean = 5.0
    geometric mean = Does not Exist
    harmonic mean = -40.0 
    
    >>> am_gm_hm(0,20)
    arithmetic mean = 10
    geometric mean = 0.0
    harmonic mean = Does not exist 
    '''
    #aritmetic mean
    print('aritmetic mean =', (a+b)/2)
    
    #geometric mean
    if a < 0 or b < 0:
        print('geometric mean = Does not Exist')
    else:
        gm = (a * b) ** 0.5
        print('harmonic mean =', gm)
    
    #harmonic mean
    if a == 0 or b == 0:
        print('harmonic mean = Does not Exist')
    else:
        hm = 2/((1/a) + (1/b))
        print('harmonic mean =', hm)

#Question 2###################################################################
def check_triangle_inequality(a, b, c):
    '''
    (number, number, number)

    Finds if a triangle is valid with the given length of 
    sides.

    >>> check_triangle_inequality(10,20,30)
    Triangle is not possible

    >>> check_triangle_inequality(20,20,30)
    Triangle is possible

    >>> check_triangle_inequality(-10,20,30)
    Triangle is not possible

    >>> check_triangle_inequality(0,30,30)
    Triangle is not possible
    '''
    
    if a+b > c and a+c > b and b+c > a:
        print('Triangle is possible')
    else:
        print('Triangle is not possible')

#Question 3###################################################################
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

#Question 4###################################################################
def check_substring(string1,string2):
    '''(string, string) -> bool

    Returns True if string 2 is a substring of string 1,
    else returns false.

    >>> check_substring('alchemy', 'chem')
    True

    >>> check_substring('alchemy', 'chemi')
    False
    '''

    return string2 in string1

#Question 5###################################################################
def generate_substrings(string):
    '''
    (string) -> list of strings

    >>> generate_substrings('alchemy')

    >>> generate_substrings('skadoosh')

    '''
    lst = list()
    for i in range(len(string)):   
        for j in range(i, len(string)):
            #print(string[i:j+1])
            if string[i:j+1] not in lst:
                lst.append(string[i:j+1])
    print(lst)

#Question 6###################################################################
def greet_me():
    '''
    Takes in a string(name) as an input, and generates a personalised
    greeting message.

    >>> greet_me()
    Enter your name: Aneesh
    Hello Aneesh, how is your day going?
    '''

    name = input('Enter your name: ')
    print('Hello', name + ', how is your day going?')

#Question 7###################################################################
def mean_calculator():
    '''
    Takes in two floating point numbers as input and 
    prints their arithmetic, geometric and harmonic means.

    >>> mean_calculator()
    Enter first number : 10
    Enter second number: 20
    arithmetic mean = 15.0
    geometric mean  = 14.142135623730951
    harmonic mean   = 13.333333333333332
    
    >>> mean_calculator()
    Enter first number : -10
    Enter second number: 20
    arithmetic mean = 5.0
    geometric mean  = Does not Exist
    harmonic mean   = -40.0
    '''

    a = float(input('Enter first number : '))
    b = float(input('Enter second number: '))
    am_gm_hm(a, b)

#Question 8###################################################################
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

#Question 9###################################################################
def fibonacci(n):
    '''(integer) -> integer
    Returns the nth term of the fibonacci series

    Precondition: n should be an integer greater than zero

    >>> fibonacci(10)
    55

    '''

    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

#Question 10###################################################################
def fibonacci_loop(n):
    '''
    Prints all terms up to the nth term of the fibonacci series

    Precondition: n should be an integer
    >>> fibonacci(10)
    

    >>> fibonacci(-1)
    Invalid input, terminating program...

    >>> fibonacci(0)
    Invalid input, terminating program...
    '''
    
    if n <= 0:
        print('Invalid input, terminating program...')
        quit()
    
    for i in range(n):
        print(fibonacci(i))

#Question 11###################################################################
def sum_game(value):
    ''' (number)

    Takes a value as input, asks for numbers and sums them up as long as the value
    is not reached.

    >>> sum_game(100)
    Enter number 1 : 10
    0 + 10.0 = 10.0
    Enter number 2 : -300
    10.0 + -300.0 = -290.0
    Enter number 3 : 400
    -290.0 + 400.0 = 110.0
    '''

    if value < 0:
        print('Invalid input, terminating program...')
        quit()

    s = 0
    i = 0
    while s < value:
        string = 'Enter number ' + str(i+1) + ' : ' 
        t = float(input(string))
        print(str(s) + ' + ' + str(t) + ' = ' + str(s+t))
        s += t
        i += 1

#Question 12###################################################################
def list_overlap(list1, list2):
    '''
    (list, list) -> list

    Returns a list of common elements of list1 and list2.

    >>> list_overlap([1, 2 , 3, 'a'], [2, 7, 'a', 100, 5, 3])
    [2, 3, 'a']


    list_overlap(['bcd', 2 , 'b', 3, 'a'], [2, 7, 'a', 'b'])
    [2, 'b', 'a']

    '''

    lst = list()

    for i in range(len(list1)):
        if list1[i] in list2:
            lst.append(list1[i])
    
    for j in range(len(list2)):
        if list2[j] in list1 and list2[j] not in lst:
            lst.append(list2[j])
    return lst
