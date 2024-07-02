from binary_tree import Node, Leaf

def df_search(tree,x):
    if tree.is_leaf():
        return tree
    if x == tree.val:
        return tree
    tmp = df_search(tree.left, x)
    if not tmp.is_leaf():
        return tmp
    return df_search(tree.right, x)

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
r = df_search(n11, 2)
print(r.str())
r = df_search(n11, 0)
print(r.str())
