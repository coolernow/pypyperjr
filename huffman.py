from pstack import Stack

class Node:
    def __init__(self, k, v):
        self.parent=None
        self.key=k
        self.value=v
        self.left_child=None
        self.right_child=None

class Node2:
    def __init__(self, l, w):
        self.parent=None
        self.key=l
        self.value=w
        self.left_child=None
        self.right_child=None

def build_freq_table(input_str):
    freq_dict={}

    for c in input_str:
        if c in freq_dict:
            cur_freq = freq_dict[c]
            freq_dict[c] = cur_freq + 1
        else:
            freq_dict[c] = 1
    return freq_dict



def rec_traverse(node, encoding, lookup_table):
    if node.left_child is None and node.right_child is None:
        lookup_table[node.value]=encoding

    if node.left_child is not None:
        rec_traverse(
            node.left_child,
            encoding+'0',
            lookup_table)

    if node.right_child is not None:
        rec_traverse(
            node.right_child,
            encoding+'1',
            lookup_table)

def main() -> object:
    freq_table = build_freq_table('bobbychilds')
    pqueue = Stack()
    for char, freq in freq_table.items():
        pqueue.push(freq, Node(freq, char))
    while True:
        key1, node1 = pqueue.pop()
        if node1 is None:
            break
        print(key1, node1.value)
        key2, node2 = pqueue.pop()
        if node2 is None:
            root = node1
            break
        node3 = Node(key1 + key2, None)
        node3.right_child=node1
        node3.left_child=node2
        pqueue.push(node3.key, node3)
    lookup_table = {}
    rec_traverse(root, "", lookup_table)
    print (lookup_table)


if __name__ == "__main__" :
    main()

