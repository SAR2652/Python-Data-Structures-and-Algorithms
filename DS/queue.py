class Queue:
    def __init__(self, MAX = None):
        self.queue = []
        self.MAX = MAX

    def enqueue(self, x):
        if self.MAX is None:
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
