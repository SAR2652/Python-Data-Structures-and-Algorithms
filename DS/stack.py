class Stack:
    #pass an optional maximum stack size parameter MAX during declaration
    def __init__(self, MAX = None):
        self.stack = []
        self.MAX = MAX

    def push(self, x):
        if self.MAX is None:
            self.stack.append(x)
            print("{} pushed successfully into the stack.".format(x))
        else:
            if len(self.stack) == self.MAX:
                print("OVERFLOW")
            else:
                self.stack.append(x)
                print("{} pushed successfully into the stack.".format(x))

    def pop(self):
        #use implicit boolean property of list to check if stack is empty or not
        if not self.stack:
            print("UNDERFLOW")
        else:
            x = self.stack[-1]
            self.stack.pop(-1)
            return x

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def view(self):
        print("Elements currently present in the stack are : {}".format(self.stack))