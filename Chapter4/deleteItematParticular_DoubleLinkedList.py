def deleteatParticularIndex(self, index):
  if not self.head:
    return
  count = 0
  curr = self.head
  while curr:
    if count == index-1:
      temp = curr.next.next
      curr.next = temp
      temp.prev = curr
      break
    else:
      count += 1
      curr = curr.next