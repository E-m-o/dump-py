def count_alphabet(filepath, character):
    '''(string, string)

    Prints the number of occurences of character in the file located at filepath.
    Note: It is case-sensitive.

    >>> count_alphabet('romeo.txt', 'a')
    10

    >>> count_alphabet('filepath', 'abcd')
    Invalid input, terminating program...

    '''

    if len(character) > 1:
        print('Invalid input, terminating program...')
        quit()

    count = 0
    
    #print(filepath)

    with open(filepath, 'r') as fi:
        lines = fi.readlines()
    
    #print(lines)

    for line in lines:
        for char in line:
            if char == character:
                count += 1
    
    print(count)