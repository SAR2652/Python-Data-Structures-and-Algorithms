from Algorithms.sorting_algorithms import quickSort

arr = [int(x)for x in input("Enter an array of integers : ").strip().split(' ')]
n = len(arr)
arr = quickSort(arr,0,n-1)

print("Sorted Array : {}".format(arr))