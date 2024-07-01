class LinkedList:
    def __init__(self) -> None:
       self.first = None
       self.size = 0
       
    def addNodo(self, value):
        myNodo = Nodo(value=value)
        
        if self.size == 0:
            self.first = myNodo
        else:
         curren = self.first
         while curren.next != None:
              curren = curren.next
         curren.next = myNodo
        self.size +=1
        return myNodo

    def removeNodo(self, key):
        if self.size == 0:
            return -1
        curren = self.first
        
        if curren.value == key:
            self.first = curren.next
            self.size -=1
            return self.size
        
        while  curren.next.value !=  key:
            if curren.next != None:
              curren = curren.next
            if curren.next == None:
                break
        if curren.next != None:
          sigNodo = curren.next
          curren.next = sigNodo.next        
          self.size -=1
        return self.size
        
    def __len__(self):
        return self.size

    def __str__(self):
        if self.first == None:
            return "[]"
        string = "["
        curren = self.first
        if curren.next != None:       
            while curren.next != None:
                string += str(curren)
                string += " , "
                curren = curren.next
        string += str(curren) +  "]"
        return string
    