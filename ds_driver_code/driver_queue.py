from DS.queue import Queue

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
        q = Queue(m)
        break
    elif choice.lower() == "no":
        q = Queue()
        break
    else:
        print("Invalid choice! Try again...")

while True:
    n = int(input("Enter your choice : "))
    if n == 1:
        x = input("Enter an element to enqueue into the queue : ")
        q.enqueue(x)
    elif n == 2:
        x = q.dequeue()
        print("Element {} dequeued from queue.".format(x))
    elif n == 3:
        x = q.peek()
        print("Element at the end of queue : {}".format(x))
    elif n == 4:
        q.view()
    elif n == 5:
        break
    else:
        print("Invalid choice. Try again.")
