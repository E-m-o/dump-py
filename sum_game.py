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