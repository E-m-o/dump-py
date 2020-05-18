def write_to_file(filepath):
    '''(string)

    Runs a REPL loop and writes the input given to the file line by line 
    till the exit command is given.

    If n is the input at the exit question, the program prompts to check
    if 'exit' is to be appended to the file.

    >>> write_to_file('romeo.txt')
    -> blah blah blah
    -> gibberish input here
    -> exit
    -----------------------------------------------
    Are you sure you want to exit the program?(y/n)
    -----------------------------------------------
    -> y
    -----------------------------------------------
                  Exiting program
    -----------------------------------------------


    >>> write_to_file('romeo.txt')
    -> blah blah blah
    -> gibberish input here
    -> exit
    -----------------------------------------------
    Are you sure you want to exit the program?(y/n)
    -----------------------------------------------
    -> n
    -----------------------------------------------
    Do you want to append exit to the file?(y/n)
    -----------------------------------------------
    -> n 
    -> bla bla bla
    -> exit
    -----------------------------------------------
    Are you sure you want to exit the program?(y/n)
    -----------------------------------------------
    -> y
    -----------------------------------------------
                  Exiting program
    -----------------------------------------------
    '''
    line = ''
    e = 'n'        

    with open(filepath, 'a') as fo:
        while True:
            line = input('-> ')
            if line == 'exit':
                e = input('-----------------------------------------------\nAre you sure you want to exit the program?(y/n)\n-----------------------------------------------\n-> ')
            
                if e == 'y':
                    print('-----------------------------------------------\n                  Exiting program\n-----------------------------------------------''')
                    fo.close()
                    #with open(filepath, 'r') as fi:
                    #    print(fi.read())
                    quit()
                else:
                    x = input('-----------------------------------------------\nDo you want to append \'exit\' to the file?(y/n)\n-----------------------------------------------\n-> ')
            
                if x == 'y':
                    continue
            fo.write('\n' + line)