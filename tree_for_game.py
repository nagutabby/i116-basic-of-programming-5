from binary_tree import Node, Leaf
from enumeration import Thing
from game import game

n1 = Node(Thing.Stone, Leaf(), Leaf())
n2 = Node(Thing.Poison, Leaf(), Leaf())
n3 = Node(Thing.Stone, n1, n2)
n4 = Node(Thing.Silver, Leaf(), Leaf())
n5 = Node(Thing.Silver, Leaf(), Leaf())
n6 = Node(Thing.Stone, n4, n5)
n7 = Node(Thing.Stone, n3, n6)

n1 = Node(Thing.Poison, Leaf(), Leaf())
n2 = Node(Thing.Stone, Leaf(), Leaf())
n3 = Node(Thing.Stone, n1, n2)
n4 = Node(Thing.Silver, Leaf(), Leaf())
n5 = Node(Thing.Gold, Leaf(), Leaf())
n6 = Node(Thing.Stone, n4, n5)
n8 = Node(Thing.Silver, n3, n6)

n1 = Node(Thing.Stone, Leaf(), Leaf())
n2 = Node(Thing.Stone, Leaf(), Leaf())
n3 = Node(Thing.Stone, n1, n2)
n4 = Node(Thing.Stone, Leaf(), Leaf())
n5 = Node(Thing.Stone, Leaf(), Leaf())
n6 = Node(Thing.Stone, n4, n5)
n9 = Node(Thing.Stone, n3, n6)

n1 = Node(Thing.Stone, Leaf(), Leaf())
n2 = Node(Thing.Poison, Leaf(), Leaf())
n3 = Node(Thing.Stone, n1, n2)
n4 = Node(Thing.Silver, Leaf(), Leaf())
n5 = Node(Thing.Silver, Leaf(), Leaf())
n6 = Node(Thing.Stone, n4, n5)
n10 = Node(Thing.Stone, n3, n6)

n11 = Node(Thing.Stone, n7, n8)
n12 = Node(Thing.Stone, n9, n10)

n1 = Node(Thing.Poison, Leaf(), Leaf())
n2 = Node(Thing.Stone, Leaf(), Leaf())
n3 = Node(Thing.Stone, n1, n2)
n4 = Node(Thing.Silver, Leaf(), Leaf())
n5 = Node(Thing.Silver, Leaf(), Leaf())
n6 = Node(Thing.Stone, n4, n5)
n7 = Node(Thing.Stone, n3, n6)

n1 = Node(Thing.Stone, Leaf(), Leaf())
n2 = Node(Thing.Poison, Leaf(), Leaf())
n3 = Node(Thing.Stone, n1, n2)
n4 = Node(Thing.Silver, Leaf(), Leaf())
n5 = Node(Thing.Silver, Leaf(), Leaf())
n6 = Node(Thing.Stone, n4, n5)
n8 = Node(Thing.Silver, n3, n6)

n1 = Node(Thing.Stone, Leaf(), Leaf())
n2 = Node(Thing.Silver, Leaf(), Leaf())
n3 = Node(Thing.Stone, n1, n2)
n4 = Node(Thing.Stone, Leaf(), Leaf())
n5 = Node(Thing.Stone, Leaf(), Leaf())
n6 = Node(Thing.Stone, n4, n5)
n9 = Node(Thing.Stone, n3, n6)

n1 = Node(Thing.Silver, Leaf(), Leaf())
n2 = Node(Thing.Stone, Leaf(), Leaf())
n3 = Node(Thing.Stone, n1, n2)
n4 = Node(Thing.Silver, Leaf(), Leaf())
n5 = Node(Thing.Silver, Leaf(), Leaf())
n6 = Node(Thing.Stone, n4, n5)
n10 = Node(Thing.Stone, n3, n6)

n13 = Node(Thing.Stone, n7, n8)
n14 = Node(Thing.Stone, n9, n10)

n15 = Node(Thing.Stone, n11, n12)
n16 = Node(Thing.Stone, n13, n14)
n17 = Node(Thing.Stone, n15, n16)

game(n17, Thing.Gold, 25)
