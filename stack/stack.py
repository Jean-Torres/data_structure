from algorithms.algorithms import searchBinary, sort

class Stack:
  def __init__(self) -> None:
      self.__stack = []
      self.__size = 0

  def push(self, value):
     list = [] + self.__stack
     if searchBinary(sort(list), value) != -1:
        return False
     self.__size +=1
     self.__stack += [value]
     return self.__stack
  
  def pop(self):
      self.__size -=1
      return self.__stack.pop()
  
  def __str__(self) -> str:
     stack = "["
     for i in range(len(self.__stack)):
        stack += str(self.__stack[i])
        if i < len(self.__stack)-1:
           stack += ", "
     stack += "]"
     return stack

  def __len__(self) -> int:
     return self.__size
  
  def peekToop(self):
     return self.__stack[self.__size-1]
  def isEmpty(self):
     return self.__size == 0