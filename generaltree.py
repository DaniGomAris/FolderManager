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
        # Buscar recursivamente en los hijos del nodo actual
        for child in current.children:
          self.insert(value, parent, child)
    else:
      self.root = Node(value)


  def delete(self, value, parent=None, current=None):
        if current is None:
            current = self.root

        if current:
            if parent is None and current.value == value:
                # Eliminar el nodo raíz
                self.root = None
                return True
            elif current.value == parent:
                # Verificar si el nodo a eliminar es un hijo del nodo actual
                for child in current.children:
                    if child.value == value:
                        current.children.remove(child)
                        return True
                # Si el nodo a eliminar no se encuentra entre los hijos, buscar recursivamente en los hijos
                for child in current.children:
                    if self.delete(value, parent, child):
                        return True
        return False
  
  
  def edit(self, old_value, new_value, current=None):
        if current is None:
            current = self.root

        if current:
            if current.value == old_value:
                current.value = new_value
                return True
            else:
                # Buscar recursivamente en los hijos
                for child in current.children:
                    if self.edit(old_value, new_value, child):
                        return True
        return False
