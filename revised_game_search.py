from queue import Queue
from game_status import Exhausted, Poison, NotFound
from enumeration import Thing

def revised_game_search(tree,x,times) -> None:
    queue: Queue = Queue()
    queue.enqueue(tree)
    while not queue.is_empty():
        if times <= 0:
            raise Exhausted('You are exhausted.')
        times = times - 1
        node = queue.top()
        queue.dequeue()
        if node.is_leaf(): # type: ignore
            continue
        if node.val == Thing.Poison: # type: ignore
            raise Poison('You found Poison.')
        if x == node.val: # type: ignore
            print('Success!')
            print('You found ', node.val, '.') # type: ignore
            return None
        queue.enqueue(node.left) # type: ignore
        queue.enqueue(node.right) # type: ignore
        queue.shuffle()
    raise NotFound('Nothing was found.')
