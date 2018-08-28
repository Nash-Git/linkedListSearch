
# Node class to create a node in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class creates a linked list and defines the operations on the linked list
class LinkedList:
    def __init__(self):
        self.head = None

# inserts node at the end of the list
    def insertNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode

# print the list in forward direction
    def printList(self):
        if self.head == None:
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, ' ', end="")
            currentNode = currentNode.next

# returns true is the target appears in the list, returns false otherwise
    def searchList(self, target):
        if self.head is None:
            return False
        currentNode = self.head
        while currentNode is not None:
            if target == currentNode.data:
                return True
            currentNode = currentNode.next
        return False