from stack.stack import Stack
from fifo.fifo import Fifo
stack = Stack()

print(stack.isEmpty())
stack.push(3)
stack.push(2)
stack.push(9)
stack.push(9)
stack.push(6)
stack.push(8)
print(stack.isEmpty())
print(stack.peekToop())

print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
(stack.pop())
print(stack)
(stack.pop())
print(stack)

print(stack.__len__())

#filas

fifo = Fifo()
(fifo.push(10))
(fifo.push(20))
(fifo.push(21))
(fifo.push(19))
(fifo.push(12))
(fifo.push(14))

      
print(fifo)
(fifo.pop())
print(fifo)
(fifo.pop())
print(fifo)
(fifo.pop())
print(fifo)
(fifo.pop())
print(fifo)
(fifo.pop())

print(fifo)
