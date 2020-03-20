from Algorithms.sorting_algorithms.insertion_sort import InsertionSort

arr = [int(x) for x in input("Enter an array of integers : ").strip().split(' ')]
arr = InsertionSort(arr)

print("Sorted Array : {}".format(arr))
