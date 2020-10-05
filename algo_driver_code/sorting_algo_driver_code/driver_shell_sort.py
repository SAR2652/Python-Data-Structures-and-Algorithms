from Algorithms.sorting_algorithms import shellSort

arr = [int(x)for x in input("Enter an array of integers : ").strip().split(' ')]
n = len(arr)
shellSort(arr, 0, n - 1)

print("Sorted Array : {}".format(arr))