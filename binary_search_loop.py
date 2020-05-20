import math as m
def binary_search_loop(L, k):
    '''(list, number) -> Bool

    Returns True if the number k exists in the list L.

    >>> binary_search_loop([1,2,3,4,5,6,7,8,9,10,11,16,19,88,457,890,1000,1245,1356], 457)
    True

    >>> binary_search_loop([1,2,3,4,5,6,7,8,9,10,11,16,19,88,457,890,1000,1245,1356], 45)
    False
    '''
    n = len(L)
    l = 0
    r = n - 1
    while l <= r:

        mid = m.floor((l+r)/2)

        if L[mid] < k:
            l = mid + 1            
    
        elif k < L[mid]: 
            r = mid - 1
    
        else:
            return True

    return False