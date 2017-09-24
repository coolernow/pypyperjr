class Link:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.key = key

class Stack:
    def __init__(self):
        self.head = None

    def push(self, key, value):
        link = Link(value)
        if self.head is None:
            self.head = link
        elif link.key < self.head.key:
            link.next = self.head
            self.head = link
        else:
            add_after(self.head, link)

    def pop(self):
        if self.head is None:
            return None
        head_link=self.head
        self.head=head_link.next
        return head_link.key, head_link.value


def add_after(before, add):
    if before.next is None:
        before.next = link
    elif link.key < before.next.key:
        link.next = before.next
        before.next = to_add
    else:
        add_after(before.next, to_add)

def main():
    stack=Stack()
    stack.push(27, 2)
    stack.push(1, 1000)
    stack.push(4, 4)
    stack.push(7, 11)
    stack.push(3, 33)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

main()