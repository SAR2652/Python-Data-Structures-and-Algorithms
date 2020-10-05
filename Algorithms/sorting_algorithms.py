def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def InsertionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp

    return arr


def SelectionSort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def heapify(arr, n, i): 
    largest = i   
    l = 2 * i + 1      
    r = 2 * i + 2      
  

    if l < n and arr[i] < arr[l]: 
        largest = l 
  

    if r < n and arr[largest] < arr[r]: 
        largest = r 
  

    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  
  

        heapify(arr, n, largest) 
  

def heapSort(arr): 
    n = len(arr) 
  

    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
  

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]    
        heapify(arr, i, 0)

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0      
    j = 0      
    k = l      
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  

def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for large l and h 
        m = (l + (r - 1)) // 2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m + 1, r) 
        merge(arr, l, m, r)

def shellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n / 2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped order
    # so keep adding one more element until the entire array is gap sorted 
    while gap > 0: 
  
        for i in range(gap, n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j - gap] >temp: 
                arr[j] = arr[j - gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap /= 2