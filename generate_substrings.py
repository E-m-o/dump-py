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
