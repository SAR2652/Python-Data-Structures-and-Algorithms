from DS.stack import Stack

print("Stack Operations :")
print("1. PUSH operation")
print("2. POP operation")
print("3. PEEK operation")
print("4. Display all the elements currently in the stack")
print("5. Exit")

while True:
    choice = input(
        "Would you like to enter a maximum capacity for stack (yes / no) : ")
    if choice.lower() == "yes":
        m = int(input("Enter maximum capacity for stack : "))
        s = Stack(m)
        break
    elif choice.lower() == "no":
        s = Stack()
        break
    else:
        print("Invalid choice! Try again...")

while True:
    n = int(input("Enter your choice : "))
    if n == 1:
        x = input("Enter an element to push into the stack : ")
        s.push(x)
    elif n == 2:
        x = s.pop()
        print("Element {} popped off from stack.".format(x))
    elif n == 3:
        x = s.peek()
        print("Element at the top of stack : {}".format(x))
    elif n == 4:
        s.view()
    elif n == 5:
        break
    else:
        print("Invalid choice. Try again.")
