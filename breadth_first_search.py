from binary_tree import Node, Leaf
from queue import Queue

def breadth_first_search(tree, x: int):
    queue: Queue = Queue()
    queue.enqueue(tree)
    while not queue.is_empty():
        node = queue.top()
        queue.dequeue()
        if node.is_leaf(): # type: ignore
            continue
        if x == node.val: # type: ignore
            return node
        queue.enqueue(node.left) # type: ignore
        queue.enqueue(node.right) # type: ignore
    return Leaf()

n1: Node = Node(1, Leaf(), Leaf())
n2: Node = Node(2, Leaf(), Leaf())
n3: Node = Node(3, n1, n2)
n4: Node = Node(4, Leaf(), Leaf())
n5: Node = Node(5, Leaf(), Leaf())
n6: Node = Node(6, n4, n5)
n7: Node = Node(7, n3, n6)
n8 = Node(8, Leaf(), Leaf())
n9 = Node(9, Leaf(), Leaf())
n10 = Node(10, n8, n9)
n11 = Node(11, n7, n10)
print(n11.str())
r = breadth_first_search(n11, 2)
print(r.str())
r = breadth_first_search(n11, 0)
print(r.str())
