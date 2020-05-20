def bubble_sort(mylist):
    '''(list) -> list

    Returns a sorted version of the input list mylist using bubble sort algorithm.

    >>> bubble_sort([2,10,15,5,4,20,6,8,9, 'a'])
    Invalid input, list elements should be of the same type

    >>> bubble_sort([2,10,15,5,4,20,6,8,9])
    [2, 4, 5, 6, 8, 9, 10, 15, 20]
    '''
    try:
        for k in range(len(mylist)):
            for i in range(len(mylist) - k -1):
                if mylist[i] > mylist[i+1]:
                    temp = mylist[i]
                    mylist[i] = mylist[i+1]
                    mylist[i+1] = temp
        return mylist
    except:
        print('Invalid input, list elements should be of the same type')