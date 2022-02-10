class Node:
  def __init__(self,data=None):
    self.item = data
    self.next = None
    self.prev = None



class DoubleLinkedList:
  def __init__(self):
    self.start_node = None
    self.end_node = None

  def insert(self,data):

    if self.start_node is None:
      new_node = Node(data)
      self.start_node = new_node

  def insert_at_end(self,data):

    if self.start_node is None:
      new_node = Node(data)
      self.start_node = new_node
      self.end_node = self.start_node
      return
    
    new_node = Node(data)
    

    self.end_node.next = new_node
    new_node.prev = self.end_node
    
    self.end_node = new_node

  def search_node(self,data):

    s_n = self.start_node
    while s_n.next is not None:
      if s_n.item == data:
        print("Item found")
        return s_n
      s_n = s_n.next
    if s_n is None:
      print("Data not found")

  def insert_at_beginning(self,data):
    new_node = Node(data)
    if self.start_node == None:
      self.start_node = new_node
      return
    self.start_node.prev = new_node
    new_node.next = self.start_node
    self.start_node = new_node
    self.end_node = new_node
    
    



