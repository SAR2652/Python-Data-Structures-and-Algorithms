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