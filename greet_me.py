def greet_me():
    '''
    Takes in a string(name) as an input, and generates a personalised
    greeting message.

    >>> greet_me()
    Enter your name: Aneesh
    Hello Aneesh, how is your day going?
    '''

    name = input('Enter your name: ')
    print('Hello', name + ', how is your day going?')
