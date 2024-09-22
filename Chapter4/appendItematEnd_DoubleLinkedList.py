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

  def addAtTheEnd(self, val):
    newNode = Node(val)
    if not self.head and not self.tail:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      newNode.prev=self.tail
      self.tail =  newNode



ll = DoubleLinkedList()
ll.addElementAtBeginning(3)
ll.addElementAtBeginning(2)
ll.addElementAtBeginning(1)
ll.addAtTheEnd(4)

ll.print()