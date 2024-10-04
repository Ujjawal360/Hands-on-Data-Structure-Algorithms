def deleteLastItemwithTail(self):
  if not self.head:
    return 
  else:
    curr = self.tail
    temp = curr.prev
    temp.next = None
    self.tail = temp

def deleteLastItemwithoutTail(self):
  if not self.head:
    return 
  else:
    curr = self.head
    while curr.next.next:
      curr = curr.next
    curr.next = None