from binary_tree import Node, Leaf

def bf_search(tree,x):
    qu = Queue()
    qu.enqueue(tree)
    while not qu.is_empty():
        node = qu.top()
        qu.dequeue()
        if node.is_leaf():
            continue
        if x == node.val:
            return node
        qu.enqueue(node.left)
        qu.enqueue(node.right)
    return Leaf()

n1 = Node(1, Leaf(), Leaf())
n2 = Node(2, Leaf(), Leaf())
n3 = Node(3, n1, n2)
n4 = Node(4, Leaf(), Leaf())
n5 = Node(5, Leaf(), Leaf())
n6 = Node(6, n4, n5)
n7 = Node(7, n3, n6)
n8 = Node(8, Leaf(), Leaf())
n9 = Node(9, Leaf(), Leaf())
n10 = Node(10, n8, n9)
n11 = Node(11, n7, n10)
print(n11.str())
r = bf_search(n11, 2)
print(r.str())
r = bf_search(n11, 0)
print(r.str())
