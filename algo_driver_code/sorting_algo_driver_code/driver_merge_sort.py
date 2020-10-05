from Algorithms.sorting_algorithms import mergeSort

arr = [int(x) for x in input("Enter an array of integers : ").strip().split(' ')]
n = len(arr)
arr = mergeSort(arr,0,n-1)

print("Sorted Array : {}".format(arr))