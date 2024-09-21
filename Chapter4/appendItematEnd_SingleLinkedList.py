# adding item to the end of the linked List
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, val):
    newNode = Node(val)
    if self.head == None:
      self.head = newNode
    else:
      current = self.head
      while current.next != None:
        current = current.next
      current.next = newNode

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
