class SimpleLinkedList:
    def __init__(self):
        self.start = None

    def traverse_list(self):
        ptr = self.start
        if ptr is None:
            print("Linked List is Empty")
            return
        else:
            print("Start", end = '')
            while ptr is not None:
                print(" -> {}".format(ptr.data), end = '')
                ptr = ptr.next
        print()

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
        elif self.start.data == pre:
            self.insert_node_at_ll_start(node)
        else:
            preptr = None
            ptr = self.start

            while ptr.data != pre:
                preptr = ptr
                ptr = ptr.next

            preptr.next = node
            node.next = ptr

    def insert_node_after_value(self, node, post):
        if self.start == None:
            print("List is empty, so inserting element at the start of list...")
            self.start = node
        else:
            ptr = self.start
            postptr = ptr.next

            while ptr.data != post:
                ptr = postptr
                postptr = postptr.next
                
            ptr.next = node
            node.next = postptr

    def delete_node_at_ll_start(self):
        if self.start == None:
            return None
        else:
            val = self.start.data
            ptr = self.start.next
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
