from DS.stack import Stack

arr = [int(x) for x in input("Enter a list of numbers : ").strip().split(' ')]

s = Stack()

for item in arr:
    s.push(item)

for i in range(0, len(arr)):
    arr[i] = s.pop()

print("Reversed Array : {}".format(arr))