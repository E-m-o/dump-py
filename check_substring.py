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
