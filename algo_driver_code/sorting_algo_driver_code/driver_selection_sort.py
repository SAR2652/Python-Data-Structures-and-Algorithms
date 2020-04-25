from Algorithms.sorting_algorithms.selection_sort import SelectionSort

arr = [int(x)
       for x in input("Enter an array of integers : ").strip().split(' ')]
arr = SelectionSort(arr)

print("Sorted Array : {}".format(arr))
