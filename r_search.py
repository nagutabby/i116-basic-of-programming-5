from queue import Queue
from enumeration import Thing
from binary_tree import Node, Leaf

def r_search(tree, x: Thing):
    queue: Queue = Queue()
    queue.enqueue(tree)
    while not queue.is_empty():
        node = queue.top()
        queue.dequeue()
        if isinstance(node, Node):
            print(node.val)
        if node.is_leaf(): # type: ignore
            continue
        if x == node.val: # type: ignore
            return node
        queue.enqueue(node.left) # type: ignore
        queue.enqueue(node.right) # type: ignore
        queue.shuffle()
    return Leaf()

