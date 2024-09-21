class Node:

  def __init__(self, val):
    self.val = val
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, val):
    newNode = Node(val)
    if not self.head and not self.tail:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode

  def print(self):
    current = self.head
    while current != None:
      print(f"{current.val} --> ", end=" ")
      current = current.next


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print()
