def LinearSearch(arr, x):
    pos = None
    for i in arr:
        if i == x:
            pos = arr.index(x)

    return pos

def BinarySearch(arr, beg, end, x):
    if end >= beg:
        mid = beg + (end - beg) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            BinarySearch(arr, beg, mid - 1, x)
        else:
            BinarySearch(arr, mid + 1, end, x)
    else:
        return None
