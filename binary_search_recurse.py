def binary_search_recurse(L, k):
    '''(list, number) -> Bool

    Returns True if the number k exists in the list L.

    >>> binary_search_recurse([1,2,3,4,5,6,7,8,9,10,11,16,19,88,457,890,1000,1245,1356], 457)
    True

    >>> binary_search_recurse([1,2,3,4,5,6,7,8,9,10,11,16,19,88,457,890,1000,1245,1356], 45)
    False
    '''
    mid = len(L)//2
    #print(L)
    if k == L[mid]:
        #print('1st flag')
        return True
    
    elif k < L[mid]:
        #print('2nd flag')
        #print(lst)
        lst = L[:mid+1]
        return binary_search_recurse(lst, k)
    
    elif k > L[mid]: 
        #print('3rd flag')
        lst = L[mid+1:]
        #print(lst)
        return binary_search_recurse(lst, k)
    
    else:
        return False

