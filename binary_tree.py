from __future__ import annotations

class Tree():
    def is_leaf(self) -> None | bool:
        pass
    def str(self) -> None | str:
        pass

class Leaf(Tree):
    def is_leaf(self) -> bool:
        return True
    def str(self) -> str:
        return 'leaf'

class Node(Tree):
    def __init__(self, v: int | str, lt: Leaf | Node, rt: Leaf | Node):
        self.val = v
        self.left = lt
        self.right = rt
    def is_leaf(self) -> bool:
        return False
    def str(self) -> str:
        return '(val: ' + str(self.val) + ') (left: ' + self.left.str() + ') (right: ' + self.right.str() + ')'

n1: Node = Node(1, Leaf(), Leaf())
n2: Node = Node(2, Leaf(), Leaf())
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
