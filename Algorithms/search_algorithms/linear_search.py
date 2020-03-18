def LinearSearch(arr, x):
    pos = None
    for i in arr:
        if i == x:
            pos = arr.index(x)
    
    return pos