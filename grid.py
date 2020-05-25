def grid(height = 1, width = 1):
    '''(integer, integer)
    Prints a grid pattern with height and width equal to the input
    provided.
    Funcion can be called using parameters directly.
    Takes default values of height and width as 1.
    Will not ask for an input if parameters are passed.

    >>> grid() 
    Enter height of the grid
    3
    Enter width of the grid
    4
     --- --- --- --- 
    |   |   |   |   |
     --- --- --- --- 
    |   |   |   |   |
     --- --- --- --- 
    |   |   |   |   |
     --- --- --- --- 
    
    >>> grid() 
    Enter height of the grid
    hdh
    Invalid input

    >>> grid()
    Enter height of the grid
    1,2,4,5
    Invalid input

    >>> grid()
    Enter height of the grid
    exit
    ...Terminating program... 
    '''
    while True:
        
        print('-------------------------------------------------------------')
        #height and width assignment
        h = input('Enter height of grid\n')
        #check if user wants to change the values and then assign
        if h != '':
            #exiting condition
            if h == 'x' or h == 'exit':
                print('...Terminating program...')
                quit()

            w = input('Enter width of grid\n')

            try:
                height = int(h)
                width = int(w)
            except:
                print('Invalid input, enter integer values\n')
                continue
        
        #print(height,width)
        h_loops = 2*height + 1
        w_loops = width
        dash_str = ' ---'
        pipe_str = '|   '

        #loop for number of strings/lines
        for i in range(h_loops):
            string = ''
            #loop for making the strings
            if i % 2 == 0:
                for j in range(w_loops):
                    string += dash_str
                print(string)
            else:
                for j in range(w_loops+1):
                    string += pipe_str
                print(string)