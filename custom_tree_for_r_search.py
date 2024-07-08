from binary_tree import Node, Leaf
from enumeration import Thing
from r_search import r_search

n4 = Node(Thing.Poison, Leaf(), Leaf())
n5 = Node(Thing.Silver, Leaf(), Leaf())
n2 = Node(Thing.Gold, n4, n5)
n6 = Node(Thing.Nothing, Leaf(), Leaf())
n3 = Node(Thing.Gold, Leaf(), n6)
n1 = Node(Thing.Nothing, n2, n3)

r = r_search(n1, Thing.Gold)
print(r.str())
