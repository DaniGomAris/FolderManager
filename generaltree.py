from File_and_Folder import File, Folder

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def is_folder(self):
        return isinstance(self.value, Folder)
    
    def is_file(self):
        return isinstance(self.value, File)

class GeneralTree:
    def __init__(self):
        self.root = None

    def get_node_icon(self, node):
        if isinstance(node.value, Folder):
            return "📁 " + node.value.name # Emoji para carpeta
        elif isinstance(node.value, File):
            return "📄 " + node.value.name  # Emoji para archivo
        else:
            return str(node.value)

    def add_node(self, value, parent=None, current=None):
        if current is None:
            current = self.root

        if current:
            if current.value == parent:
                # Verificar si ya existe un nodo con el mismo nombre
                if not self.duplicate_name(value.name):
                    current.children.append(Node(value))
                else:
                    print(f"El nombre ya existe: '{value.name}'")
            else:
                # Buscar recursivamente en los hijos del nodo actual
                for child in current.children:
                    self.add_node(value, parent, child)
        else:
            # Verificar si ya existe un nodo con el mismo nombre
            if not self.duplicate_name(value.name):
                self.root = Node(value)
            else:
                print(f"El nombre ya existe: '{value.name}'")
    

    def delete_node(self, value, parent=None, current=None) -> bool:
        if current is None:
            current = self.root

        if current:
            # Buscar el nodo con el valor y el padre (si se proporciona)
            for child in current.children:
                if (parent is None and child.value.name == value) or (child.value.name == parent and child.value.name == value):
                    # Eliminar el nodo y sus descendientes
                    current.children.remove(child)
                    return True

            # Buscar recursivamente en los hijos del nodo actual
            for child in current.children:
                if self.delete_node(value, parent, child):
                    return True

        return False
    

    def find_node_by_name(self, name, current=None):
        if current is None:
            current = self.root

        if current:
            if current.value.name == name:
                # El nodo actual tiene el nombre deseado
                return current
            else:
                # Buscar recursivamente en los hijos y sus descendientes
                for child in current.children:
                    result = self.find_node_by_name(name, child)
                    if result:
                        return result

        # Si no se encuentra el nodo con el nombre, devolver False
        return None
        

    def rename_node(self, old_name, new_name):
        node_to_rename = self.find_node_by_name(old_name)

        if node_to_rename is not None:
            # Verificar si es un Folder o un File y cambiar el nombre en consecuencia
            if node_to_rename.is_folder():
                node_to_rename.value.name = new_name
            elif node_to_rename.is_file():
                node_to_rename.value.name = new_name

            return True
        else:
            return False
    
    def duplicate_name(self, original_name):
        return self.find_node_by_name(original_name) is not None

    def pretty_print_tree(self, node = None, linea=""):
        if self.root is None:
            print("Empty tree")
            return

        if node is None:
            node = self.root

        print(linea + " └───" + self.get_node_icon(node))

        for child in node.children:
            self.pretty_print_tree(child, linea + "     ")


"""
carpeta_1 = Folder("carpeta 1")
carpeta_2 = Folder("carpeta 2")
carpeta_3 = Folder("carpeta 3")
carpeta_4 = Folder("carpeta 4")

archivo = File("archivo")

arbol = GeneralTree()
arbol.add_node(carpeta_1)

arbol.add_node(archivo, carpeta_1)
arbol.add_node(carpeta_2, carpeta_1)
arbol.add_node(archivo, carpeta_1)
arbol.add_node(archivo, carpeta_1)

arbol.add_node(archivo, carpeta_2)
arbol.add_node(carpeta_3, carpeta_2)
arbol.add_node(archivo, carpeta_2)

arbol.add_node(archivo, carpeta_3)
arbol.add_node(archivo, carpeta_3)
arbol.add_node(carpeta_4, carpeta_3)

arbol.add_node(archivo, carpeta_4)
arbol.add_node(archivo, carpeta_4)
arbol.add_node(archivo, carpeta_4)

arbol.pretty_print_tree()

arbol.delete_node("carpeta 3")

arbol.pretty_print_tree()
"""