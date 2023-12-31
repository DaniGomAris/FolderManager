import os
import zipfile
import random

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
        """
        Obtiene una representación visual (icono) para el nodo basado en su tipo
        """        
        if isinstance(node.value, Folder):
            return "📁 " + node.value.name # Emoji para carpeta
        elif isinstance(node.value, File):
            return "📄 " + node.value.name  # Emoji para archivo
        else:
            return str(node.value)

    def add_node(self, value, parent = None, current = None):
        """
        Añade un nodo al árbol
        """
        # Si no se especifica el nodo actual, comienza desde el nodo raíz
        if current is None:
            current = self.root

        # Verifica si el nodo actual coincide con el nodo padre especificado
        if current:
            if current.value == parent:
                # Añade el nodo a los hijos del padre
                current.children.append(Node(value))
            else:
                # Busca recursivamente en los hijos del nodo actual
                for child in current.children:
                    self.add_node(value, parent, child)
        else:
            self.root = Node(value)
    

    def delete_node(self, value, parent = None, current = None) -> bool:
        """
        Elimina un nodo del árbol
        """
        # Si no se especifica el nodo actual, comienza desde el nodo raíz
        if current is None:
            current = self.root

        # Verifica si el nodo actual tiene hijos con el nombre y padre dados
        if current:
            for child in current.children:
                # Elimina el hijo si coincide con los criterios de búsqueda
                if (parent is None and child.value.name == value) or (child.value.name == parent and child.value.name == value):
                    current.children.remove(child)
                    return True

            # Busca recursivamente en los hijos del nodo actual
            for child in current.children:
                if self.delete_node(value, parent, child):
                    return True

        # Retorna False si no se encuentra el nodo con el nombre
        return False
    

    def find_node_by_name(self, name, current = None):
        """
        Encuentra un nodo en el árbol basado en su nombre
        """
        # Si no se especifica el nodo actual, comienza desde el nodo raíz
        if current is None:
            current = self.root

        if current:
            # Verifica si el nodo actual tiene el nombre que se busca
            if current.value.name == name:
                return current
            else:
                # Busca recursivamente en los hijos del nodo actual
                for child in current.children:
                    result = self.find_node_by_name(name, child)
                    if result:
                        return result

        # Retorna False si no encuentra un nodo con el nombre 
        return False
        

    def rename_node(self, old_name, new_name) -> bool:
        """
        Renombra un nodo en el árbol
        """
        # Busca el nodo a modificar por su nombre utilizando otro metodo
        node_to_rename = self.find_node_by_name(old_name)

        # Si el nodo existe, verifica si es una carpeta o archivo
        if node_to_rename is not None: 
            if node_to_rename.is_folder():
                node_to_rename.value.name = new_name
            elif node_to_rename.is_file():
                node_to_rename.value.name = new_name

            return True
        else:
            # Si no existe, retorna False
            return False
    
    def duplicate_name(self, original_name) -> bool:
        """
        Verifica si ya hay otro nodo con el mismo nombre en el arbol
        """
        return self.find_node_by_name(original_name) is not None
    
    def node_data(self, node):
        """
        Obtiene información sobre un nodo en formato de diccionario
        """
        if node.is_folder():
            print()
            return {
                "Type": "Folder",
                "Name": node.value.name,
                "Size": node.value.size,
                "Creation Date": node.value.creation_date
            }
        elif node.is_file():
            print()
            return {
                "Type": "File",
                "Name": node.value.name,
                "Size": node.value.size,
                "Creation Date": node.value.creation_date
            }
        
    def build_tree_from_zip(self, zip_file_path):
        """
        Construye una estructura de árbol desde un archivo ZIP
        """
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Lista de contenidos en el archivo ZIP
            zip_contents = zip_ref.namelist()

            # Nombre de la carpeta raíz del archivo ZIP
            root_folder_name = os.path.basename(zip_ref.filename)

            # Crea el valor para la carpeta raíz del árbol
            root_folder_value = Folder(root_folder_name, random.randint(1,20), "12/08/2023")
            root_node = Node(root_folder_value)

            # Recorre los elementos en el archivo ZIP
            for item in zip_contents:
                # Nombre del elemento
                item_name = os.path.basename(item)

                # Tamaño y la fecha de creación del elemento
                item_size = zip_ref.getinfo(item).file_size
                item_creation_date = zip_ref.getinfo(item).date_time

                # Divide el nombre del elemento en partes con '/'
                path_parts = item.split('/')
                current_node = root_node

                # Recorre las partes del path, creando nodos si es necesario
                for part in path_parts[:-1]:
                    child_node = None

                    # Busca un nodo hijo con el mismo nombre
                    for child in current_node.children:
                        if child.value.name == part:
                            child_node = child
                            break

                    # Si no encuentra el nodo, lo crea y lo agrega como hijo
                    if not child_node:
                        folder_value = Folder(part, 0, None)
                        child_node = Node(folder_value)
                        current_node.children.append(child_node)

                    # Establece el nodo actual como el nodo hijo recién creado
                    current_node = child_node

                # Si el elemento tiene un nombre, crea un nodo de archivo y lo agrega como hijo
                if item_name:
                    file_node = Node(File(item_name, random.randint(1,20), "12/08/2023"))
                    current_node.children.append(file_node)

        # Establece el nodo raíz del arbol construido
        self.root = root_node


    def pretty_print_tree(self, node = None, linea = ""):
        """
        Imprime una representación visual del árbol
        """
        if self.root is None:
            print("Empty tree")
            return

        if node is None:
            node = self.root

        print(linea + " └───" + self.get_node_icon(node))

        for child in node.children:
            self.pretty_print_tree(child, linea + "     ")
    

"""
# Ejemplo arbol propio
carpeta_1 = Folder("carpeta 1", 12414141, 423423)
carpeta_2 = Folder("carpeta 2", 12414141, 423423)
carpeta_3 = Folder("carpeta 3", 12414141, 423423)
carpeta_4 = Folder("carpeta 4", 12414141, 423423)

archivo = File("archivo", 12414141, 423423)
archivo1 = File("archivo1", 12414141, 423423)
archivo2 = File("archivo2", 12414141, 423423)
archivo3 = File("archivo3", 12414141, 423423)
archivo4 = File("archivo4", 12414141, 423423)
archivo5 = File("archivo5", 12414141, 423423)
archivo6 = File("archivo6", 12414141, 423423)
archivo7 = File("archivo7", 12414141, 423423)
archivo8 = File("archivo8", 12414141, 423423)
archivo9 = File("archivo9", 12414141, 423423)
archivo10 = File("archivo10", 12414141, 423423)

arbol = GeneralTree()
arbol.add_node(carpeta_1)

arbol.add_node(archivo1, carpeta_1)
arbol.add_node(carpeta_2, carpeta_1)
arbol.add_node(archivo2, carpeta_1)
arbol.add_node(archivo3, carpeta_1)

arbol.add_node(archivo4, carpeta_2)
arbol.add_node(carpeta_3, carpeta_2)
arbol.add_node(archivo5, carpeta_2)

arbol.add_node(archivo6, carpeta_3)
arbol.add_node(archivo7, carpeta_3)
arbol.add_node(carpeta_4, carpeta_3)

arbol.add_node(archivo8, carpeta_4)
arbol.add_node(archivo9, carpeta_4)
arbol.add_node(archivo10, carpeta_4)

arbol.pretty_print_tree()

arbol.create_folder_from_tree()
"""

"""
# Ejemplo arbol .zip
arbol = GeneralTree()

arbol.build_tree_from_zip("ejemplo.zip")

arbol.rename_node("ejemplo.zip", "Hola")

arbol.pretty_print_tree()

arbol.create_folder_from_tree()
"""