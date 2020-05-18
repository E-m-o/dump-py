def list_overlap(list1, list2):
    '''
    (list, list) -> list

    Returns a list of common elements of list1 and list2.

    >>> list_overlap([1, 2 , 3, 'a'], [2, 7, 'a', 100, 5, 3])
    [2, 3, 'a']


    list_overlap(['bcd', 2 , 'b', 3, 'a'], [2, 7, 'a', 'b'])
    [2, 'b', 'a']

    '''

    lst = list()

    for i in range(len(list1)):
        if list1[i] in list2:
            lst.append(list1[i])
    
    for j in range(len(list2)):
        if list2[j] in list1 and list2[j] not in lst:
            lst.append(list2[j])
    return lst
