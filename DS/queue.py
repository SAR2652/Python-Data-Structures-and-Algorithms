class Queue:
    def __init__(self, MAX = None):
        self.queue = []
        self.MAX = MAX

    def enqueue(self, x):
        if self.MAX == None:
            self.queue.append(x)
            print("Element {} enqueued successfully into the queue.".format(x))
        else:
            if len(self.queue) == self.MAX:
                print("OVERFLOW")
            else:
                self.queue.append(x)
                print("Element {} enqueued successfully into the queue.".format(x))

    def dequeue(self):
        #use implicit boolean property of list to check if stack is empty or not
        if not self.queue:
            print("UNDERFLOW")
        else:
            x = self.queue[0]
            self.queue.pop(0)
            return x

    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None

    def view(self):
        print("Elements currently present in the queue are : {}".format(self.queue))


class LinkedQueue:
    def __init__(self, MAX = None):
        self.front = None
        self.rear = None
        self.MAX = MAX

    def check_queue_length(self):
        if self.front == None:
            return 0
        elif self.front == self.rear:
            return 1
        else:
            ptr = self.front
            count = 1
            while ptr.next != self.rear:
                ptr = ptr.next
                count += 1
            return count


    def enqueue(self, node):
        if self.MAX == None:
            if self.front == None:
                self.front = node
                self.rear = self.front
            else:
                if self.front == self.rear:
                    self.front.next = node
                    self.rear = self.front.next
                else:
                    self.rear.next = node
                    self.rear = self.rear.next
        else:
            if self.front == None:
                self.front = node
                self.rear = self.front
            else:
                if self.front == self.rear:
                    self.front.next = node
                    self.rear = self.front.next
                elif self.check_queue_length() < self.MAX:
                    self.rear.next = node
                    self.rear = self.rear.next

    def dequeue(self):
        val = -1
        if self.front == None:
            print("UNDERFLOW!!!")
        elif self.front == self.rear:
            val = self.front.data
            self.front = None
            self.rear = None
        else:
            ptr = self.front
            self.front = self.front.next
            val = ptr.data
            ptr = None
        return val

    def peek(self):
        val = -1
        if self.front == None:
            print("Linked Queue is empty!!!")
        else:
            val = self.front.data
        return val
    
    def display(self):
        if self.front == None:
            print("Linked Queue is Empty!!!")
            return
        ptr = self.front
        print("Front ->", end = ' ')
        while ptr != self.rear:
            print("{} ->".format(ptr.data), end = ' ')
            ptr = ptr.next
        print("{} -> Rear".format(self.rear.data))
