class SimpleLinkedList:
    def __init__(self):
        self.start = None

    def traverse_list(self):
        ptr = self.start
        if ptr is None:
            print("Linked List is Empty")
            return
        while ptr is not None:
            print(ptr.data, end = ' ')
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
