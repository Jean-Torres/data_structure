from .nodo import Nodo 

class Fifo:
    def __init__(self):
        self.first = None
        self.size = 0

    def push(self, value):
        nodo = Nodo(value)
        self.size +=1
        if self.first == None:
            self.first = nodo
            return self.size

        curren = self.first
        while curren.next != None:
            curren = curren.next
        curren.next = nodo
        return self.size

    def pop(self):
        if self.size == 0:
            return -1
        curren = self.first
        self.first = self.first.next
        self.size -=1 
        return curren
    
    def __str__(self): 
        curren = self.first
        if curren == None:
            return "[]"

        fifo = "["
        if curren.next != None:
            while curren.next != None:
                fifo += str(curren)
                if curren.next != None:
                    fifo += ","
                curren = curren.next
        fifo += str(curren) +  "]"
        return fifo

