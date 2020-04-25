from Algorithms.search_algorithms import LinearSearch

arr = [int(x) for x in input("Enter an array of integers : ").strip().split(' ')]
n = int(input("Enter a number to search within the array : "))

pos = LinearSearch(arr, n)

if pos == None:
    print("Element {} not found in array.".format(n))
else:
    print("Element {} found in array at index {}.".format(n, pos))