from LickedList import LinkedList
myList = LinkedList()

myList.addNodo(8)
myList.addNodo(-299)
myList.addNodo(5)
myList.addNodo(2)
myList.addNodo(100)
myList.addNodo(9)
myList.addNodo(6)
myList.addNodo(0)
myList.addNodo(1)
myList.addNodo(200)
myList.addNodo(3)



#Add inicio
myList.addNodoFirst(23)
myList.addNodoFirst(19)
myList.addNodoFirst(-5)

#Invert list
myList.invertList()

#Search
#print(myList.search(2))

print(myList)
#Sort
myList.sortNode()  
print(myList)

