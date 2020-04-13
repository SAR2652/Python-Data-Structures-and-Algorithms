from DS.stacks.linked_stack import LinkedStack
from DS.linked_lists.linked_list_nodes import Node 

print("Stack Operations :")
print("1. PUSH operation")
print("2. POP operation")
print("3. PEEK operation")
print("4. Display all the elements currently in the stack")
print("5. Exit")

while True:
    choice = input("Would you like to enter a maximum capacity for stack (yes / no) : ")
    if choice.lower() == "yes":
        m = int(input("Enter maximum capacity for stack : "))
        ls = LinkedStack(m)
        break
    elif choice.lower() == "no":
        ls = LinkedStack()
        break
    else:
        print("Invalid choice! Try again...")

while True:
    n = int(input("Enter your choice : "))
    if n == 1:
        x = int(input("Enter an element to push into the stack : "))
        node = Node(x)
        ls.push(node)
    elif n == 2:
        x = ls.pop()
        if x != None:
            print("Element {} popped off from stack.".format(x))
    elif n == 3:
        x = ls.peek()
        if x != None:
            print("Element at the top of stack : {}".format(x))
        else:
            print("Stack is empty!")
    elif n == 4:
        ls.display()
    elif n == 5:
        break
    else:
        print("Invalid choice. Try again.")
