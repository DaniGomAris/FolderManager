import sys
import os

from File_and_Folder import Folder
from Menu import Menu
from GeneralTree import GeneralTree
from Program import Program

if __name__ == "__main__":
    while True:
        print("""
---------Folder Manager---------
1. Start  
2. Exit""")
        option = int(input("Option: "))

        if option == 1:
            while True:
                print("""
----------Start option----------
1. Extract .zip  
2. Create own Tree 
3. exit""")
                option_menu = int(input("Option: "))
                print("--------------------------------")

                if option_menu == 1: # Extraer .zip para el arbol
                    print()

                    zip_file_name = input("Enter the name of the zip file: ")
                    zip_file_path = os.path.join(os.path.dirname(__file__), zip_file_name + ".zip")  # Construye la ruta completa al archivo .zip

                    print()
                    print("--------------------------------")
                    print()

                    # Construir el arbol a partir del archivo zip
                    tree = GeneralTree()
                    tree.build_tree_from_zip(zip_file_path)
                    tree.pretty_print_tree()

                    # Crear un programa con el árbol construido
                    program = Program(tree)
                    menu = Menu(program)
                    menu.show_menu()
                
                elif option_menu == 2: # Crear un arbol propio
                    print()

                    root_folder_name = input("Enter the name of the root folder: ")
                    root_folder_size = input(f"Enter the size of the '{root_folder_name}' folder: ")
                    root_folder_date = input(f"Enter the name of the '{root_folder_name}' folder: ")

                    print()
                    print("--------------------------------")
                    print()

                    # Construir el arbol a partir de la carpeta creada
                    tree = GeneralTree()
                    tree.add_node(Folder(root_folder_name, root_folder_size, root_folder_date))
                    tree.pretty_print_tree()

                    # Crear un programa con el árbol construido
                    program = Program(tree)
                    menu = Menu(program)
                    menu.show_menu()

                elif option == 3:
                    sys.exit()

                else:
                    print("incorrect option, try again")
                    continue

        elif option == 2:
            sys.exit()

        else:
            print("incorrect option, try again")
            continue