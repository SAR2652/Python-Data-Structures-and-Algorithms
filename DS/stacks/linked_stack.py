from DS.linked_lists.linked_list_nodes import Node

class LinkedStack:
    def __init__(self, MAX=None):
        self.top = None
        self.MAX = MAX

    def count_stack_elements(self):
        if self.top == None:
            return 0
        else:
            ptr = self.top
            count = 1
            while ptr.next != None:
                ptr = ptr.next
                count += 1

            return count

    def insert_node(self, node):
        node.next = self.top
        self.top = node

    def push(self, node):
        if self.MAX == None:
            self.insert_node(node)
            print("Element {} pushed successfully into the stack.".format(node.data))
        else:
            if self.count_stack_elements() == self.MAX:
                print("OVERFLOW!!!")
                return
            else:
                self.insert_node(node)
                print("Element {} pushed successfully into the stack.".format(node.data))

    def pop(self):
        val = None
        if self.top == None:
            print("UNDERFLOW")
        else:
            val = self.top.data
            self.top = self.top.next
        return val

    def peek(self):
        if self.top != None:
            return self.top.data
        else:
            return None

    def display(self):
        if self.top == None:
            print("Stack is empty!")
        else:
            print("Elements currently present in the stack are :")
            ptr = self.top
            print("Top -> ", end = ' ')
            while ptr.next != None:
                print("{} -> ".format(ptr.data), end = ' ')
                ptr = ptr.next
            print("{}".format(ptr.data))
