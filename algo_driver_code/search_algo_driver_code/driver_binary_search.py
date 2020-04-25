from Algorithms.search_algorithms import BinarySearch

arr = [int(x) for x in input("Enter the elements in the array : ").split(' ')]

arr = sorted(arr)
print("Sorted Array : {}".format(arr))

n = int(input("Enter a number to search within the array : "))

pos = BinarySearch(arr, 0, len(arr) - 1, n)

if pos != None:
    print("Element {} found at index {} within the array.".format(n, pos))
else:
    print("Element {} was not found in the array.".format(n))

