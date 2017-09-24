class Link:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,value):
        link = Link(value)
        if self.head is not None:
            link.next = self.head
        self.head = link

    def pop(self):
        if self.head is None:
            return None
        head_link=self.head
        self.head=head_link.next
        return head_link.value

def main():
    stack=Stack()
    stack.push(27)
    stack.push(1)
    stack.push(4)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

main()

