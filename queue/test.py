class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.in_stack=[]
        self.out_stack=[]
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.in_stack.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[len(self.out_stack)-1]

def main():
    q = MyQueue()
    q.push(1)
    print q.pop()
    q.push(2)
    q.push(3)
    print q.top()
    print q.pop()

if __name__ == '__main__':
    main()