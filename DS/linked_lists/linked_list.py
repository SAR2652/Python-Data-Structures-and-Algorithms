class SimpleLinkedList:
    def __init__(self):
        self.start = None

    def traverse_list(self):
        ptr = self.start
        if ptr is None:
            print("Linked List is Empty")
            return
        else:
            print("Start", end='')
            while ptr != None:
                print(" -> {}".format(ptr.data), end='')
                ptr = ptr.next
        print(" -> End")


    def insert_node_at_ll_start(self, node):
        if self.start == None:
            self.start = node
        else:
            node.next = self.start
            self.start = node


    def insert_node_at_ll_end(self, node):
        if self.start == None:
            self.start = node
        else:
            ptr = self.start

            while ptr.next != None:
                ptr = ptr.next

            ptr.next = node


    def insert_node_before_value(self, node, pre):
        if self.start == None:
            print("List is empty, so inserting element at the start of list...")
            self.start = node
            return 1
        elif self.start.data == pre:
            self.insert_node_at_ll_start(node)
            return 1
        else:
            preptr = None
            ptr = self.start

            while ptr != None and ptr.data != pre:
                preptr = ptr
                ptr = ptr.next

            if ptr == None:
                print("Value {} does not exist within list.".format(pre))
                return 0

            preptr.next = node
            node.next = ptr
            return 1


    def insert_node_after_value(self, node, post):
        if self.start == None:
            print("List is empty, so inserting element at the start of list...")
            self.start = node
            return 0
        else:
            ptr = self.start
            postptr = ptr.next

            while ptr != None and ptr.data != post:
                ptr = postptr
                postptr = postptr.next

            if ptr == None:
                print("Value {} does not exist within list.".format(post))
                return 0

            ptr.next = node
            node.next = postptr
            return 1


    def delete_node_at_ll_start(self):
        if self.start == None:
            return None
        else:
            val = self.start.data
            ptr = self.start.next
            self.start = None
            self.start = ptr
            return val


    def delete_node_at_ll_end(self):
        if self.start == None:
            return None
        else:
            preptr = None
            ptr = self.start

            while ptr.next != None:
                preptr = ptr
                ptr = ptr.next

            val = ptr.data
            preptr.next = None
            return val


    def delete_node_before_value(self, pre):
        flag = None
        if self.start == None:
            print("List is empty, so try another time...")
            return flag
        elif self.start.data == pre:
            print("No element before starting element {}".format(pre))
            return flag
        else:
            preptr = None
            ptr = self.start

            while ptr.next.data != pre and ptr != None:
                preptr = ptr
                ptr = ptr.next

            if ptr != None:
                val = ptr.data
                preptr.next = ptr.next
                ptr = None
                return val
            else:
                return flag


    def delete_node_after_value(self, post):
        flag = None
        if self.start == None:
            print("List is empty, so try another time...")
            return flag
        else:
            ptr = self.start
            postptr = ptr.next

            while postptr != None and ptr.data != post:
                ptr = postptr
                postptr = postptr.next

            if ptr.data == post and ptr.next == None:
                print("No value present in list after element {}".format(post))
                return None

            if ptr == None:
                print("No value {} present within the list".format(post))
                return None

            val = postptr.data
            ptr.next = postptr.next
            postptr = None
            return val


    def clear_linked_list(self):
        if self.start == None:
            print("List is already empty!")
        else:
            ptr = self.start
            while ptr != None:
                self.delete_node_at_ll_start()
                ptr = self.start

    
    def bubble_sort(self):
        if self.start == None:
            print("Linked List is already empty")
        else:
            outerptr = self.start
            while outerptr.next != None:
                innerptr = outerptr.next
                while innerptr != None:
                    if innerptr.data < outerptr.data:
                        temp = outerptr.data
                        outerptr.data = innerptr.data
                        innerptr.data = temp
                    innerptr = innerptr.next
                outerptr = outerptr.next

                

class CircularLinkedList:
    def __init__(self):
          self.start = None

    def traverse_list(self):
        ptr = self.start
        if ptr is None:
            print("Linked List is Empty")
            return
        else:
            print("Start", end='')
            while ptr.next != self.start:
                print(" -> {}".format(ptr.data), end='')
                ptr = ptr.next
        print(" -> {} -> Start".format(ptr.data))


    def insert_node_at_cll_start(self, node):
        if self.start == None:
            self.start = node
            self.start.next = self.start
        else:
            node.next = self.start
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
            ptr.next = node
            self.start = node


    def insert_node_at_cll_end(self, node):
        if self.start == None:
            self.start = node
        else:
            ptr = self.start

            while ptr.next != self.start:
                ptr = ptr.next

            ptr.next = node
            node.next = self.start

    def insert_node_before_value(self, node, pre):
        if self.start == None:
            print("List is empty, so inserting element at the start of list...")
            self.start = node
            return 1
        elif self.start.data == pre:
            self.insert_node_at_cll_start(node)
            return 1
        else:
            preptr = None
            ptr = self.start

            while ptr.next != self.start and ptr.data != pre:
                preptr = ptr
                ptr = ptr.next

            if ptr == None:
                print("Value {} does not exist within list.".format(pre))
                return 0

            preptr.next = node
            node.next = ptr
            return 1


    def insert_node_after_value(self, node, post):
        if self.start == None:
            print("List is empty, so inserting element at the start of list...")
            self.start = node
            return 0
        else:
            ptr = self.start
            postptr = ptr.next

            while ptr.next != self.start and ptr.data != post:
                ptr = postptr
                postptr = postptr.next

            if ptr.next == self.start and ptr.data != post:
                print("Value {} does not exist within list.".format(post))
                return 0

            ptr.next = node
            node.next = postptr
            return 1


    def delete_node_at_cll_start(self):
        if self.start == None:
            return None
        else:
            val = self.start.data
            ptr = self.start
            nextptr = self.start.next
            while ptr.next != self.start:
                ptr = ptr.next
            self.start = nextptr
            ptr.next = nextptr
            return val

    def delete_node_at_cll_end(self):
        if self.start == None:
            return None
        else:
            preptr = None
            ptr = self.start

            while ptr.next != self.start:
                preptr = ptr
                ptr = ptr.next

            val = ptr.data
            ptr = None
            preptr.next = self.start
            return val


    def delete_node_before_value(self, pre):
        flag = None
        if self.start == None:
            print("List is empty, so try another time...")
            return flag
        elif self.start.data == pre:
            print("No element before starting element {}".format(pre))
            return flag
        else:
            preptr = self.start
            ptr = self.start.next

            while ptr.data != pre and ptr.next.data != pre and ptr != self.start:
                preptr = ptr
                ptr = ptr.next

            if ptr.data == pre:
                return self.delete_node_at_cll_start()

            if ptr != self.start:
                val = ptr.data
                preptr.next = ptr.next
                ptr = None
                return val
            else:
                return flag


    def delete_node_after_value(self, post):
        flag = None
        if self.start == None:
            print("List is empty, so try another time...")
            return flag
        elif self.start.data == post:
            val = self.start.next.data
            self.start.next = self.start.next.next
            return val
        else:
            ptr = self.start
            postptr = ptr.next

            while ptr.data != post and postptr != self.start:
                ptr = postptr
                postptr = postptr.next

            if postptr.data == post and ptr.next == self.start:
                print("No value present in list after element {}".format(post))
                return None

            if ptr == self.start:
                print("No value {} present within the list".format(post))
                return None

            val = postptr.data
            ptr.next = postptr.next
            postptr = None
            return val

    def clear_circular_linked_list(self):
        if self.start == None:
            print("List is already empty!")
        else:
            ptr = self.start
            while ptr.next != self.start:
                self.delete_node_at_cll_start()
                ptr = ptr.next
            ptr = None
            self.start = None

    def bubble_sort(self):
        if self.start == None:
            print("Linked List is already empty")
        else:
            outerptr = self.start
            while outerptr.next != self.start:
                innerptr = outerptr.next
                while innerptr != self.start:
                    if innerptr.data < outerptr.data:
                        temp = outerptr.data
                        outerptr.data = innerptr.data
                        innerptr.data = temp
                    innerptr = innerptr.next
                outerptr = outerptr.next

class DoublyLinkedList:
    def __init__(self):
        self.start = None

    def traverse_list(self):
        if self.start == None:
            print("Doubly Linked List is empty!!!")
        else:
            ptr = self.start
            print("Start ->", end = ' ')
            while ptr.next != None:
                print("{} -> ".format(ptr.data), end = ' ')
                ptr = ptr.next
            print("{} -> End".format(ptr.data))

    def insert_node_at_dll_start(self, node):
        if self.start == None:
            self.start = node
        else:
            node.next = self.start
            self.start.prev = node
            self.start = node
        print("Element {} was successfully inserted into the doubly linked list.".format(node.data))

    def insert_node_at_dll_end(self, node):
        if self.start == None:
            self.start = node
        else:
            ptr = self.start
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = node
            node.prev = ptr
        print("Element {} was successfully inserted into the doubly linked list.".format(node.data))

    def insert_node_before_value(self, node, pre):
        flag = None
        if self.start.data == pre:
            self.insert_node_at_dll_start(node)
            flag = 1
        else:
            ptr = self.start
            while ptr.next != None and ptr.data != pre:
                ptr = ptr.next
            if ptr != None:
                preptr = ptr.prev
                preptr.next = node
                node.prev = preptr
                node.next = ptr
                ptr.prev = node
                flag = 1
                print("Element {} was successfully inserted before node with value {} into the doubly linked list.".format(node.data, pre))
        return flag

    def insert_node_after_value(self, node, post):
        flag = None
        if self.start == None:
            print("Doubly Linked List is empty, so no value like {} exists in it.".format(post))
            print("Inserting element with value {} at the beginning of the list".format(post))
            self.start = node
            flag = 1
        else:    
            ptr = self.start
            while ptr.next != None and ptr.data != post:
                ptr = ptr.next
            if ptr != None:
                postptr = ptr.next
                ptr.next = node
                node.prev = ptr
                node.next = postptr
                postptr.prev = node
                flag = 1
                print("Element {} was successfully inserted after the node with value {} into the doubly linked list.".format(node.data, post))
        return flag

    def delete_node_at_dll_start(self):
        val = None
        if self.start != None:
            ptr = self.start
            self.start = self.start.next
            self.start.prev = None
            val = ptr.data
            return val
        else:
            return val
        
    def delete_node_at_dll_end(self):
        val = None
        if self.start != None:
            ptr = self.start
            while ptr.next != None:
                ptr = ptr.next
            val = ptr.data
            ptr.prev.next = None
            ptr = None
            return val

    def delete_node_before_value(self, pre):
        val = None
        if self.start == None:
            print("Doubly Linked List is empty!!!")
        else:
            if self.start.data == pre:
                print("Element {} is located at the beginning of the list so operation could not be performed".format(pre))
                return -1
            else:
                ptr = self.start
                while ptr.next.data != pre:
                    ptr = ptr.next
                if ptr != None:
                    preptr = ptr.prev
                    preptr.next = ptr.next
                    if ptr.next != None:
                        preptr.next.prev = preptr
                    val = ptr.data
                else:
                    print("Node with value {} does not exist within the list.".format(pre))
                    val = -2
        return val

    def delete_node_after_value(self, post):
        val = None
        if self.start == None:
            print("Doubly Linked List is empty!!!")
        else:
            ptr = self.start
            while ptr.next != None and ptr.data != post:
                ptr = ptr.next
            if ptr != None:
                if ptr.next == None:
                    print("Element {} is the last element in the linked list, so operation failure occured")
                else:
                    val = ptr.next.data
                    postptr = ptr.next.next
                    ptr.next = postptr
                    postptr.prev = ptr
            else:
                print("Node with value {} does not exist within the list")
                val = -2
        return val

    def clear_linked_list(self):
        if self.start == None:
            print("List is already empty!")
        else:
            while self.start.next != None:
                self.delete_node_at_dll_start()
            self.start = None
