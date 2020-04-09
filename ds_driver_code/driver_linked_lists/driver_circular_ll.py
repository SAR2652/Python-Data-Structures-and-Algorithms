from DS.linked_lists.linked_list import CircularLinkedList
from DS.linked_lists.linked_list_nodes import Node

cll = CircularLinkedList()
print("An empty Circular Linked List has been initialized.")

print("List of Operations :")
print("1. Traverse Circular Linked List")
print("2. Insert Node at the start of Circular Linked List")
print("3. Insert Node at the end of Circular Linked List")
print("4. Insert Node before a node with given value in the Circular Linked List")
print("5. Insert Node after a node with given value in the Circular Linked List")
print("6. Delete Node at the start of Circular Linked List")
print("7. Delete Node at the end of Circular Linked List")
print("8. Delete Node before a node with given value in the Circular Linked List")
print("9. Delete Node after a node with given value in the Circular Linked List")
print("10. Delete all elements from the list")
print("11. Exit")

while True:

    choice = int(input("Enter choice of operation : "))

    if choice == 1:
        cll.traverse_list()

    elif choice == 2:
        n = int(input("Enter a numerical value to insert as a node into the list : "))
        node = Node(n)
        cll.insert_node_at_cll_start(node)

    elif choice == 3:
        n = int(input("Enter a numerical value to insert as a node into the list : "))
        node = Node(n)
        cll.insert_node_at_cll_end(node)

    elif choice == 4:
        n = int(input("Enter numerical value to insert as a node into the list : "))
        pre = int(input("Enter the value at its succeeding node : "))
        node = Node(n)
        flag = cll.insert_node_before_value(node, pre)
        if flag == 1:
            print(
                "Element {} successfully inserted before element {} within the list".format(n, pre))

    elif choice == 5:
        n = int(input("Enter numerical value to insert as a node into the list : "))
        post = int(input("Enter the value at its preceding node : "))
        node = Node(n)
        flag = cll.insert_node_after_value(node, post)
        if flag == 1:
            print("Element {} successfully inserted after element {} within the list".format(
                n, post))

    elif choice == 6:
        val = cll.delete_node_at_cll_start()
        if val == None:
            print("Linked List is empty!")
        else:
            print("Node with value {} was deleted from the start of list".format(val))

    elif choice == 7:
        val = cll.delete_node_at_cll_end()
        if val == None:
            print("Linked List is empty!")
        else:
            print("Node with value {} was deleted from the end of list".format(val))

    elif choice == 8:
        pre = int(
            input("Enter the value at node whose preceding node is to be deleted : "))
        val = cll.delete_node_before_value(pre)
        if val != None:
            print("Node with value {} preceding the node with value {} was deleted from the end of list".format(
                val, pre))

    elif choice == 9:
        post = int(
            input("Enter the value at node whose succeeding node is to be deleted : "))
        val = cll.delete_node_after_value(post)
        if val != None:
            print("Node with value {} succeeding the node with value {} was deleted from the end of list".format(
                val, post))

    elif choice == 10:
        cll.clear_circular_linked_list()
        print("Deleted all elements from Linked List successfully...")

    elif choice == 11:
        break

    else:
        print("Invalid choice! Try again...")
