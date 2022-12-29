from node import Node
 
class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("All out of space!")
 
  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("There are no more recipes available for this option. It's time to cook something different!")
  
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("There are no more recipes available for this option. It's time to cook something different!")
  
  def has_space(self):
    return self.limit > self.size
  
  def is_empty(self):
    return self.size == 0