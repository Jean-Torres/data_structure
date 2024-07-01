myList = LinkedList()

myList.addNodo(8)
myList.addNodo(5)
myList.addNodo(2)
myList.addNodo(9)
myList.addNodo(1)
myList.addNodo(3)

print(myList.__len__())
print(myList)
myList.removeNodo(1)
myList.removeNodo(9)
myList.removeNodo(8)
myList.removeNodo(2)
myList.removeNodo(5)
myList.removeNodo(3)
            
print(myList)
