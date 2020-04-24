from DS.queue import LinkedQueue
from DS.linked_lists.linked_list_nodes import Node

print("Queue Operations :")
print("1. ENQUEUE operation")
print("2. DEQUEUE operation")
print("3. PEEK operation")
print("4. Display all the elements currently in the queue")
print("5. Exit")

while True:
    choice = input(
        "Would you like to enter a maximum capacity for queue (yes / no) : ")
    if choice.lower() == "yes":
        m = int(input("Enter maximum capacity for queue : "))
        lq = LinkedQueue(m)
        break
    elif choice.lower() == "no":
        lq = LinkedQueue()
        break
    else:
        print("Invalid choice! Try again...")

while True:
    n = int(input("Enter your choice : "))
    if n == 1:
        x = input("Enter an element to enqueue into the queue : ")
        node = Node(x)
        lq.enqueue(node)
    elif n == 2:
        x = lq.dequeue()
        if x != -1:
            print("Element {} dequeued from queue.".format(x))
    elif n == 3:
        x = lq.peek()
        if x!= -1:
            print("Element at the end of queue : {}".format(x))
    elif n == 4:
        lq.display()
    elif n == 5:
        break
    else:
        print("Invalid choice. Try again.")
