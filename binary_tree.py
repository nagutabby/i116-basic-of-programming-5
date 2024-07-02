class Tree(object):
    def is_leaf(self):
        pass
    def str(self):
        pass

class Leaf(Tree):
    def is_leaf(self):
        return True
    def str(self):
        return 'leaf'

class Node(Tree):
    val = 0
    left = Leaf()
    right = Leaf()
    def is_leaf(self):
        return False
    def str(self):
        return '(val: ' + str(self.val) + ') (left: ' + self.left.str() + ') (right: ' + self.right.str() + ')'
    def __init__(self, v, lt, rt):
        self.val = v
        self.left = lt
        self.right = rt
