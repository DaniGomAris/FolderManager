import sys

from Menu import Menu 
from GeneralTree import GeneralTree
from Program import Program
from File_and_Folder import Folder

if __name__ == "__main__":
    print("""
---Folder Manager---
1. Start  
2. Exit
""")
    option = int(input("Option: "))

    if option == 1:
      root_folder_name = input("Enter the name of the root folder: ")
      tree = GeneralTree()
      tree.add_node(Folder(root_folder_name))
      tree.pretty_print_tree()
      program = Program(tree)
      
      menu = Menu(program)  # Crea una instancia de la clase Menu
      menu.show_menu()  # Llama al método show_menu en la instancia de Menu
    
    if option == 2:
       sys.exit()

