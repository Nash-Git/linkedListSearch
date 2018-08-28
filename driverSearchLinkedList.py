'''
This program creates a linked list with random values, and search the list for a given value
@author: Asif Nashiry
'''

from searchLinkedList import LinkedList
import random

aList = LinkedList()
numOfData = 10

for i in range(numOfData):
    data = random.randint(1,20)
    aList.insertNode(data)

aList.printList()
print('\n')
target = int(input('Enter the search element: '))
if aList.searchList(target):
    print('The target element', target, 'appears in the list')
else:
    print('The target element', target, 'does not appear in the list')
