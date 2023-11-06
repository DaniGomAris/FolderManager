import sys

from GeneralTree import GeneralTree

class Program:
    def __init__(self, tree):
        self.tree = tree
        self.folder_stack = [tree.root.value]  # Pila de carpetas visitadas, inicializada con la carpeta raíz

    def show_menu(self):
        print("""
MENU
Tienes las siguientes opciones:
1) Add folder
2) Add file
3) Edit folder
4) Edit file
5) Delete folder
6) Delete file
7) Exit""")
        self.get_menu_answer()

    def get_menu_answer(self):
        option = input("Opción: ")
        # Añadir una carpeta
        if option == "1":
            self.add_folder()

        # Añadir un archivo
        elif option == "2":
            self.add_file()

        # Editar una carpeta
        elif option == "3":
            self.edit_folder()

        # Editar un archivo
        elif option == "4":
            self.edit_file()

        # Eliminar una carpeta
        elif option == "5":
            self.delete_folder()
        
        # Eliminar un archivo
        elif option == "6":
            self.delete_file()

        elif option == "7":
            sys.exit("Adios")


    def add_folder(self):
        name = input("Folder name:")


    def add_file(self):
        name = input("File name:")

    def edit_folder(self):
        name = input("Folder name:")

    def edit_file(self):
        name = input("File name:")

    def delete_folder(self):
        name = input("Folder name:")

    def delete_file(self):
        name = input("File name:")