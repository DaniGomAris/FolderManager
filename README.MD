# Opción I:

Crearán un sistema de gestión de archivos y carpetas. Para hacerlo, seguirán estos requisitos:
- El sistema será gestionado a partir de un árbol general

- Este árbol, se creará inicialmente desde un archivo .zip entregado

- En este archivo habrá una carpeta madre con carpetas y archivos dentro

- Toda la práctica se realizará sobre las carpetas y archivos extraídos desde este archivo .zip

- El usuario podrá buscar, crear y eliminar archivos y carpetas...

- Los cambios de eliminación y adición de archivos y carpetas se deben reflejar en el árbol.

- Para hacer alguna de estas acciones el usuario le da al sistema la ruta donde se quiere realizar la acción. A esta ruta se debe llegar recorriendo el árbol sin la ayuda de las librerías de Python.

- Las librerías de Python como os y zipfile las usarán sólo para desempaquetar y crear el árbol inicial.

- Sobre el árbol responderán preguntas que tienen que ver con diversas características, como por ejemplo el peso de las carpetas, la fecha de creación de los archivos, el peso o formato de los archivos, entre otros.

- En la sustentación, les entregaré un zip y haré 5 preguntas sobre ese árbol de carpetas y archivos. 

- Ustedes, usando el código de la práctica, deberán responder a estas preguntas agregando o modificando código a su solución actual.

- Pensar en el tipo de características que deben guardar de cada nodo es parte esencial de la solución, así que piensen y pregunten mucho.

- En la medida que piensen y se preparen mejor para ese día, llegarán más rápido a la solución.

- Es clave entender el recorrido, entender de altura, de niveles y todos los conceptos que hemos venido tocando en el bloque de árboles.

def create_folder_from_tree(self, node = None, current_path = ""):
        """
        Crea una carpeta basado en la estructura del árbol
        """
        # Comienza desde el nodo raíz y la ruta vacía
        if node is None and self.root is not None:
            node = self.root

        # Construye la ruta completa del nodo en el sistema de archivos
        node_path = os.path.join(current_path, node.value.name)

        # Si el nodo es una carpeta, crea la carpeta en el sistema de archivos
        if node.is_folder():
            os.makedirs(node_path)

            # Se llama recursivamente a la funcion para los hijos
            for child in node.children:
                self.create_folder_from_tree(child, node_path)

        # Si el nodo es un archivo, crea el archivo con contenido de ejemplo
        elif node.is_file():
            with open(node_path, 'w') as fike:
                fike.write("Contenido del archivo")


def create_folder(self):
        self.tree.create_folder_from_tree()
        print()
        print("Folder create successfully")
        print("--------------------------------")
        print()
        self.tree.pretty_print_tree()

elif option == "8":
    print("--------create folder-----------")
    print()
    self.program.create_folder()
    self.show_menu()