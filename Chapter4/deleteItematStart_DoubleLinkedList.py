def deleteFirstItem(self):
  if not self.head:
    return   
  else:
    curr = self.head
    temp = curr.next
    temp.prev = None
    self.head = temp