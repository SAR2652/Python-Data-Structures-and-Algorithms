from Recursion.tower_of_hanoi import TowerOfHanoi

n = int(input("Enter the number of rings : "))

TowerOfHanoi(n, 'A', 'C', 'B')

print("Number of Steps required = {}".format(2 ** n - 1))