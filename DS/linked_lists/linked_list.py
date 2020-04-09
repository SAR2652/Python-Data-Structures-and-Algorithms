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
            while ptr is not None:
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
        print("Start")


    def insert_node_at_cll_start(self, node):
        if self.start == None:
            self.start = node
            self.start.next = self.start
        else:
            node.next = self.start
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
            ptr = self.start.next
            self.start = None
            self.start = ptr
            return val


    def delete_node_at_cll_end(self):
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

            while postptr != self.start and ptr.data != post:
                ptr = postptr
                postptr = postptr.next

            if ptr.data == post and ptr.next == self.start:
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
            while ptr != None:
                self.delete_node_at_cll_start()
                ptr = self.start

