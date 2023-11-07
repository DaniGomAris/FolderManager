import sys
import os

from Menu import Menu
from GeneralTree import GeneralTree
from Program import Program

if __name__ == "__main__":
    print("""
---------Folder Manager---------
1. Start  
2. Exit""")
    option = int(input("Option: "))
    print("--------------------------------")

    if option == 1:
        print()
        zip_file_name = input("Enter the name of the zip file, example: ejemplo.zip: ")  # El usuario ingresa el nombre del archivo .zip
        zip_file_path = os.path.join(os.path.dirname(__file__), zip_file_name)  # Construye la ruta completa al archivo .zip
        #root_folder_name = input("Enter the name of the root folder: ")
        print()
        print("--------------------------------")
        print()

        # Construir el árbol a partir del archivo zip
        tree = GeneralTree()
        tree.build_tree_from_zip(zip_file_path)
        tree.pretty_print_tree()

        # Crear un programa con el árbol construido
        program = Program(tree)
        menu = Menu(program)
        menu.show_menu()

    elif option == 2:
        # Otras opciones de salida o limpieza, si es necesario
        sys.exit("Chao")
