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

  def appendParticularIndex(self, val, index):
    newNode=Node(val)
    if not self.head:
      return
    elif index<0 and index>self.length:
      return "It cannot be done"
    elif index ==0:
      newNode.next=self.head
      self.head.prev=newNode
      self.head=newNode
    else:
      curr=self.head
      count=0
      while curr:
        if count==index-1:
          temp = curr.next
          temp.prev = newNode
          newNode.next = temp
          curr.next = newNode
          newNode.prev = curr
          break
        else:
          count += 1
          curr=curr.next

ll = DoubleLinkedList()
ll.addElementAtBeginning(3)
ll.addElementAtBeginning(2)
ll.addElementAtBeginning(1)
ll.addAtTheEnd(4)
ll.appendParticularIndex(7,2)

ll.print()