from nodo import Nodo

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

    def addNodoFirst(self, value):
        curren = self.first
        self.first = Nodo(value=value)
        self.first.next = curren
        self.size +=1
        return self.first

    def invertList(self):
        curren = self.first
        currenNext = curren.next
        curren.next = None
        currenBack = curren
        for i in range(1,self.size):
            curren = currenNext
            currenNext = curren.next
            curren.next = currenBack
            currenBack= curren
        self.first = curren

    def search(self, key):
        curren = self.first
        currens = []
        count = 0
        while curren.next != None:
            if curren.value == key:
                currens.extend([curren.value])
                count +=1
            curren = curren.next
        return [str(currens),count]

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
    
    def sortNode(self):
        current = self.first
        for i in range(self.size):
            for x in range(self.size): 
              if current.value > current.next.value:
                  if current == self.first:
                      nextNextNodo = current.next.next
                      current.next.next = current
                      self.first = current.next
                      current.next = nextNextNodo
                  elif current != self.first:
                      nextNextNodo = current.next.next
                      previuNext.next = current.next
                      current.next.next = current
                      current.next = nextNextNodo
              previuNext = current
              current = current.next
              if current == None  or current.next == None:
                  current = self.first

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
    