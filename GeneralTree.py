class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

class GeneralTree:
  def __init__(self):
    self.root = None

  def insert(self, value, parent=None, current=None):
    if current is None:
      current = self.root
    if current:
      if current.value == parent:
        current.children.append(Node(value))
      else:
        for child in current.children:
          self.insert(value, parent, child)
    else:
      self.root = Node(value)
