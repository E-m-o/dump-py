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
