class Node:
  def __init__ (self,data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__ (self):
    self.head = None

  def print_ll(self):
    n = self.head
    if n is not None:
      while n != None:
        print(n.data)
        n = n.next


  def print_middle(self):
    p1 = self.head
    p2 =self.head

    while p2 and p2.next.next:
      p1 = p1.next
      p2 = p2.next.next

    print(p1.data)


l1 = LinkedList()
l1.head = Node("first")
e = Node(data=str(1))
l1.head.next = e
for i in range(2,10):
  n = Node(data=str(i))
  e.next = n


  e = n


l1.print_ll()
l1.print_middle()
  

