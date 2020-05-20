def selection_sort(mylist):
    '''(list) -> list

    Returns a sorted version of the input list mylist using selection sort algoritm.

    >>> selection_sort([2,10,15,5,4,20,6,8,9, 'a'])
    Invalid input, list elements should be of the same type

    >>> selection_sort([2,10,15,5,4,20,6,8,9])
    [2, 4, 5, 6, 8, 9, 10, 15, 20]
    '''
    try:
        for i in range(len(mylist)-1):
            for j in range(i,len(mylist)):
                if mylist[i] > mylist[j]:
                    temp = mylist[i]
                    mylist[i] = mylist[j]
                    mylist[j] = temp
        return mylist
    except:
        print('Invalid input, list elements should be of the same type')
