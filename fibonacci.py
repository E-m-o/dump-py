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
