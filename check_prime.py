def check_prime(num):
    '''(integer) -> Bool

    Returns True if num is prime and False if it is not.

    >>> check_prime(5)
    True

    >>> check_prime(4)
    False

    '''
    if not isinstance(num, int):
        print('Invalid input, enter integer value')
        quit()

    if num <= 1:
        return 'Not Defined'
    
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True
    