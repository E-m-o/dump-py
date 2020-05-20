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
    

def find_primes(high):
    '''(integer)
    
    Prints all the numbers that are prime below high.

    >>> find_primes(10)
    2 3 5 7

    >>> find_primes(-1)
    Invalid input, enter a positive integer

    >>> find_primes(0)
    No primes exist below this number
    
    >>> find_primes(0.0)
    Invalid input, enter an integer
    '''

    if not isinstance(high, int):
        print('Invalid input, enter an integer')
        quit()
    
    if high <= 2:
        print('No primes exist below this number')
        quit()
    
    for num in range(2, high):
        if check_prime(num):
            print(num, end = ' ')

