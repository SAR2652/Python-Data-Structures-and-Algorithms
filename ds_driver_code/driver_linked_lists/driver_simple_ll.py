from DS.linked_lists.simple_linked_list import SimpleLinkedList
from DS.linked_lists.linked_list_nodes.simple_ll_node import Node

sll = SimpleLinkedList()
print("Empty Linked List has been initialized")

print("List of Operations :")
print("1. Traverse Linked List")
print("2. Insert Node at the start of Linked List")
print("3. Insert Node at the end of Linked List")
print("4. Delete Node at the start of Linked List")
print("5. Delete Node at the end of Linked List")
print("6. Search Node Operation")
print("7. Exit")

while True:

    choice = int(input("Enter choice of operation : "))

    if choice == 1:
        sll.traverse_list()

    elif choice == 2:
        n = int(input("Enter a numerical value to insert as a node into the list : "))
        node = Node(n)
        sll.insert_node_at_ll_start(node)

    elif choice == 3:
        n = int(input("Enter a numerical value to insert as a node into the list : "))
        node = Node(n)
        sll.insert_node_at_ll_end(node)

    elif choice == 4:
        val = sll.delete_node_at_ll_start()
        if val == None:
            print("Linked List is empty!")
        else:
            print("Node with value {} was deleted from the start of list".format(val))

    elif choice == 5:
        val = sll.delete_node_at_ll_end()
        if val == None:
            print("Linked List is empty!")
        else:
            print("Node with value {} was deleted from the end of list".format(val))
    
    elif choice == 7:
        break
