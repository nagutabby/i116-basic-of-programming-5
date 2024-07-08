from binary_tree import Node, Leaf

def depth_first_search(tree, x: int) -> Node | Leaf:
    if tree.is_leaf():
        return tree
    if x == tree.val:
        return tree
    tmp = depth_first_search(tree.left, x)
    if not tmp.is_leaf():
        return tmp
    return depth_first_search(tree.right, x)

n1: Node = Node(1, Leaf(), Leaf())
n2: Node  = Node(2, Leaf(), Leaf())
n3: Node = Node(3, n1, n2)
n4: Node = Node(4, Leaf(), Leaf())
n5: Node = Node(5, Leaf(), Leaf())
n6: Node = Node(6, n4, n5)
n7: Node = Node(7, n3, n6)
n8: Node = Node(8, Leaf(), Leaf())
n9: Node = Node(9, Leaf(), Leaf())
n10: Node = Node(10, n8, n9)
n11: Node = Node(11, n7, n10)
print(n11.str())
r: Node | Leaf = depth_first_search(n11, 2)
print(r.str())
r = depth_first_search(n11, 0)
print(r.str())
