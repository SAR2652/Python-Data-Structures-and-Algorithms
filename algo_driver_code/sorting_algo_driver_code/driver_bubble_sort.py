from Algorithms.sorting_algorithms.bubble_sort import BubbleSort

arr = [int(x) for x in input("Enter an array of integers : ").strip().split(' ')]

arr = BubbleSort(arr)

print("Sorted Array : {}".format(arr))