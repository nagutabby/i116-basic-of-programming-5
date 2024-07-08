from enum import Enum, auto
from binary_tree import Node, Leaf

class Thing(Enum):
    Gold: auto = auto()
    Silver: auto = auto()
    Stone: auto = auto()
    Poison: auto = auto()
    Nothing: auto = auto()

    def __str__(self) -> str:
        if self == Thing.Gold:
            return 'Gold'
        elif self == Thing.Silver:
            return 'Silver'
        elif self == Thing.Stone:
            return 'Stone'
        elif self == Thing.Poison:
            return 'Poison'
        elif self == Thing.Nothing:
            return 'Nothing'
        else:
            return 'Error'

print(Thing.Gold)
print(Thing.Silver)
print(Thing.Stone)
print(Thing.Poison)
print(Thing.Nothing)

n1: Node = Node(Thing.Poison, Leaf(), Leaf())
n2: Node = Node(Thing.Stone, Leaf(), Leaf())
n3: Node = Node(Thing.Stone, n1, n2)
n4: Node = Node(Thing.Silver, Leaf(), Leaf())
n5: Node = Node(Thing.Gold, Leaf(), Leaf())
n6: Node = Node(Thing.Stone, n4, n5)
n8: Node = Node(Thing.Silver, n3, n6)
