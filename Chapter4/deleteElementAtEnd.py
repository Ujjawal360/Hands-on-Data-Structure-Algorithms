class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, val):
    newNode = Node(val)
    if not self.head and not self.tail:
      self.head = newNode
      self.tail = newNode
      self.length += 1
    else:
      self.tail.next = newNode
      self.tail = newNode
      self.length += 1

  def insertAtIndex(self, value, index):
    if index < 0 or index > self.length:
      return "It cannot be done"

    if index == 0:
      newNode = Node(value)
      newNode.next = self.head
      self.head = newNode
      self.length += 1
    else:
      curr = self.head
      count = 0
      while curr:
        if count == index - 1:
          temp = curr.next
          newNode = Node(value)
          newNode.next = temp

          curr.next = newNode
          self.length += 1
          count += 1
        else:
          count += 1
          curr = curr.next


  def print(self):
    current = self.head
    while current != None:
      print(f"{current.val} --> ", end=" ")
      current = current.next

  def removeFirstElement(self):
    if not self.head:
      return
    else:
      current = self.head
      temp = current.next
      self.head = temp 
      self.length -= 1

#############################
  def removeLastElement(self):
    if not self.head:
      return
    else:
      curr = self.head
      while curr.next.next != None:
        curr = curr.next
      curr.next = None
      self.length -= 1
#############################

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
# my_list.insertAtIndex(4, 0)
# my_list.removeFirstElement()
my_list.removeLastElement()

my_list.print()