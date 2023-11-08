import os
import zipfile

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

    def add_node(self, value, parent = None, current = None):
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
    

    def delete_node(self, value, parent = None, current = None) -> bool:
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
    

    def find_node_by_name(self, name, current = None):
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
    
    def node_data(self, node):
        if node.is_folder():
            print()
            return {
                "Type": "Folder",
                "Name": node.value.name,
                "Size": node.value.size,
                "Creation Date": node.value.creation_date
            }
        elif node.is_file():
            return {
                "Type": "File",
                "Name": node.value.name,
                "Size": node.value.size,
                "Creation Date": node.value.creation_date
            }
        else:
            return {
                "Type": "Unknown",
                "Value": node.value
            }
        
    def build_tree_from_zip(self, zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_contents = zip_ref.namelist()
            root_folder_name = os.path.basename(zip_ref.filename)
            root_folder_value = Folder(root_folder_name, 0, None)
            root_node = Node(root_folder_value)

            for item in zip_contents:
                item_name = os.path.basename(item)
                item_size = zip_ref.getinfo(item).file_size
                item_creation_date = zip_ref.getinfo(item).date_time

                path_parts = item.split('/')
                current_node = root_node

                for part in path_parts[:-1]:
                    child_node = None
                    for child in current_node.children:
                        if child.value.name == part:
                            child_node = child
                            break

                    if not child_node:
                        folder_value = Folder(part, 0, None)
                        child_node = Node(folder_value)
                        current_node.children.append(child_node)

                    current_node = child_node

                if item_name:
                    file_node = Node(File(item_name, item_size, item_creation_date))
                    current_node.children.append(file_node)

        self.root = root_node


    def create_zip_from_tree(self, output_zip_path=None):
        """
        Crea un archivo .zip a partir del árbol actual.
        """
        output_zip_path = f"{self.root.value.name}.zip"

        with zipfile.ZipFile(output_zip_path, 'w') as zip_ref:
            nodes_to_process = [(self.root, "")]

            while nodes_to_process:
                node, current_path = nodes_to_process.pop(0)

                if node.is_file() or node.is_folder():
                    # Construir la ruta completa al nodo
                    node_path = os.path.join(current_path, node.value.name)

                    # Crear carpetas y archivos temporales si no existen
                    if node.is_folder() and not os.path.exists(node_path):
                        os.makedirs(node_path)

                    elif node.is_file() and not os.path.exists(node_path):
                        with open(node_path, 'w') as temp_file:
                            temp_file.write("Contenido del archivo temporal")

                    # Verificar si el archivo realmente existe
                    if os.path.exists(node_path):
                        # Obtener la ruta relativa desde el directorio de trabajo actual
                        arcname = os.path.relpath(node_path, start=current_path)

                        # Agregar al .zip
                        zip_ref.write(node_path, arcname=arcname)

                        # Si es una carpeta, agregar sus hijos a la lista de nodos a procesar
                        if node.is_folder():
                            nodes_to_process.extend((child, node_path) for child in node.children)


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