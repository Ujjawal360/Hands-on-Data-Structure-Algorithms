class Node:
  def __init__(self, val):
    self.val=val
    self.prev=None
    self.next=None

class DoubleLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None

  def addElementAtBeginning(self, val):
    newNode = Node(val)
    if not self.head and not self.tail:
      self.head = newNode
      self.tail = newNode
    else:
      # newNode.next = self.head // self.head.prev = newNode // self.head = newNode
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode

  def print(self):
    current = self.head
    while current != None:
      print(f"{current.val} <--> ", end=" ")
      current = current.next

ll = DoubleLinkedList()
ll.addElementAtBeginning(3)
ll.addElementAtBeginning(2)
ll.addElementAtBeginning(1)


ll.print()