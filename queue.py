import random

class Queue():
    def __init__(self) -> None:
        self.elements: list[int] = []

    def is_empty(self) -> bool:
        if self.elements == []:
            return True
        else:
            return False

    def top(self) -> None | int:
        if self.is_empty():
            return None
        else:
            return self.elements[0]

    def dequeue(self) -> None:
        if not self.is_empty():
            self.elements = self.elements[1:]

    def enqueue(self, e: int) -> None:
        self.elements = self.elements + [e]

    def str(self) -> str:
        return str(self.elements)

    def swap(self, i: int, j: int) -> None:
        if i >= 0 and j >= 0 and i < len(self.elements) and j < len(self.elements) and i != j:
            tmp: int = self.elements[i]
            self.elements[i] = self.elements[j]
            self.elements[j] = tmp

    def shuffle(self) -> None:
        size: int = len(self.elements)
        t: int = size // 2
        while t > 0:
            i: int = random.randrange(size)
            j: int = random.randrange(size)
            self.swap(i, j)
            t = t - 1

queue: Queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print(queue.str())
queue.shuffle()
print(queue.str())
