from src.lab10.structures import Stack
from src.lab10.structures import Queue

print("STACK")

s = Stack()
print("стек пустой:", s.is_empty())
s.push(1)
s.push(20)
s.push(654)
print("верх стека:", s.peek())
print("удален элемент:", s.pop())
print("новый верх:", s.peek())

print("QUEUE")

q = Queue()
print("Очередь пуста:", q.is_empty())
q.enqueue("C")
q.enqueue("0")
q.enqueue("W")
print("первый элемент:", q.peek())
print("удален элемент:", q.dequeue())
print("новый первый:", q.peek())
