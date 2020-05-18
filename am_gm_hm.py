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
