from DS.linked_lists.linked_list import DoublyLinkedList
from DS.linked_lists.linked_list_nodes import DLLNode

dll = DoublyLinkedList()
print("An empty Linked List has been initialized.")

print("List of Operations :")
print("1. Traverse Linked List")
print("2. Insert Node at the start of Linked List")
print("3. Insert Node at the end of Linked List")
print("4. Insert Node before a node with given value in the Linked List")
print("5. Insert Node after a node with given value in the Linked List")
print("6. Delete Node at the start of Linked List")
print("7. Delete Node at the end of Linked List")
print("8. Delete Node before a node with given value in the Linked List")
print("9. Delete Node after a node with given value in the Linked List")
print("10. Delete all elements from the list")
print("11. Exit")

while True:

    choice = int(input("Enter choice of operation : "))

    if choice == 1:
        dll.traverse_list()

    elif choice == 2:
        n = int(input("Enter a numerical value to insert as a node into the list : "))
        node = DLLNode(n)
        dll.insert_node_at_dll_start(node)

    elif choice == 3:
        n = int(input("Enter a numerical value to insert as a node into the list : "))
        node = DLLNode(n)
        dll.insert_node_at_dll_end(node)

    elif choice == 4:
        n = int(input("Enter numerical value to insert as a node into the list : "))
        pre = int(input("Enter the value at its succeeding node : "))
        node = DLLNode(n)
        flag = dll.insert_node_before_value(node, pre)
        if flag == -1:
            print("No element {} exists within the list".format(pre))

    elif choice == 5:
        n = int(input("Enter numerical value to insert as a node into the list : "))
        post = int(input("Enter the value at its preceding node : "))
        node = DLLNode(n)
        flag = dll.insert_node_after_value(node, post)
        if flag == None:
            print("No element {} exists within the list".format(post))

    elif choice == 6:
        val = dll.delete_node_at_dll_start()
        if val == None:
            print("Linked List is empty!!!")
        else:
            print("Node with value {} was deleted from the start of list".format(val))

    elif choice == 7:
        val = dll.delete_node_at_dll_end()
        if val == None:
            print("Linked List is empty!")
        else:
            print("Node with value {} was deleted from the end of list".format(val))

    elif choice == 8:
        pre = int(
            input("Enter the value at node whose preceding node is to be deleted : "))
        val = dll.delete_node_before_value(pre)
        if val != None and val != -1 and val != -2:
            print("Node with value {} preceding the node with value {} was deleted from the end of list".format(val, pre))

    elif choice == 9:
        post = int(
            input("Enter the value at node whose succeeding node is to be deleted : "))
        val = dll.delete_node_after_value(post)
        if val != None and val != -1:
            print("Node with value {} succeeding the node with value {} was deleted from the end of list".format(
                val, post))

    elif choice == 10:
        dll.clear_linked_list()
        print("Deleted all elements from Linked List successfully...")

    elif choice == 11:
        break

    else:
        print("Invalid choice! Try again...")
