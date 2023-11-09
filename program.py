from File_and_Folder import File, Folder
import random

class Program:
    def __init__(self, tree):
        self.tree = tree

    def add_folder(self):
        parent_folder_name = input("Type the name of the folder where you want to add a folder: ")
        folder_name = input("Folder name: ")


        parent_folder = self.tree.find_node_by_name(parent_folder_name)
        if parent_folder and parent_folder.is_folder():
            new_folder = Folder(folder_name, random.randint(1,20), "12/08/2023")
            self.tree.add_node(new_folder, parent_folder.value)
            print()
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()
        else:
            print()
            print("Parent folder not found or it's not a folder")
            print()
            self.tree.pretty_print_tree()

    def add_file(self):
        parent_folder_name = input("Type the name of the folder where you want to add a folder: ")
        file_name = input("File name: ")


        parent_folder = self.tree.find_node_by_name(parent_folder_name)
        if parent_folder and parent_folder.is_folder():
            new_folder = File(file_name, random.randint(1,20), "12/08/2023")
            self.tree.add_node(new_folder, parent_folder.value)
            print()
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()
        else:
            print()
            print("Parent folder not found or it's not a folder")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()


    def edit_folder(self):
        old_name = input("Folder name to edit: ")
        new_name = input("Folder new name: ")

        if self.tree.rename_node(old_name, new_name):
            print()
            print("Folder renamed successfully")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()
        else:
            print()
            print("Folder not found")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()


    def edit_file(self):
        old_name = input("File name to edit: ")
        new_name = input("File new name: ")

        if self.tree.rename_node(old_name, new_name):
            print()
            print("File renamed successfully")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()
        else:
            print()
            print("File not found")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()


    def delete_folder(self):
        name = input("Folder name to delete: ")

        if self.tree.delete_node(name):
            print()
            print("Folder deleted successfully")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()
        else:
            print()
            print("Folder not found")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()


    def delete_file(self):
        name = input("File name to delete: ")

        if self.tree.delete_node(name):
            print()
            print("File deleted successfully")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()
        else:
            print()
            print("File not found")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()

    def node_data(self):
        name = input("Node name: ")
        node = self.tree.find_node_by_name(name)

        if node:
            data = self.tree.node_data(node)
            print("Node Data:")
            for key, value in data.items():
                print(f"{key}: {value}")
            print()
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()
        else:
            print()
            print("Node not found")
            print("--------------------------------")
            print()
            self.tree.pretty_print_tree()

    
