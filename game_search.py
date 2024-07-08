from queue import Queue
from enumeration import Thing

def game_search(tree, x, times) -> None:
    queue: Queue = Queue()
    queue.enqueue(tree)
    while not queue.is_empty():
        if times <= 0:
            print('Failure!')
            print('You are exhausted.')
            return None
        times = times - 1
        node = queue.top()
        queue.dequeue()
        if node.is_leaf(): # type: ignore
            continue
        if node.val == Thing.Poison: # type: ignore
            print('Failure!')
            print('You found Poison.')
            return
        if x == node.val: # type: ignore
            print('Success!')
            print('You found ', node.val, '.') # type: ignore
            return
        queue.enqueue(node.left) # type: ignore
        queue.enqueue(node.right) # type: ignore
        queue.shuffle()
    print('Failure!')
    print('Nothing was found.')
