def fibonacci(n):
    '''(integer) -> integer
    Returns the nth term of the fibonacci series

    Precondition: n should be an integer greater than zero

    >>> fibonacci(10)
    34

    >>> fibonacci(-1)
    Invalid input, terminating program...

    >>> fibonacci(0)
    Invalid input, terminating program...
    '''

    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

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
