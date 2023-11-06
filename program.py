from File_and_Folder import File, Folder

class Program:
    def __init__(self, tree):
        self.tree = tree

    def add_folder(self):
        folder_name = Folder(input("Type the name of the folder where you want to add a folder: "))
        new_folder_name = Folder(input("Folder name: "))

        parent_node = self.tree.find_node_by_name(folder_name)
        if parent_node is not None and parent_node.is_folder():
            self.tree.add_node(folder_name, new_folder_name)
            print("Folder added successfully")
            self.tree.pretty_print_tree()
        else:
            print("Parent folder not found or it's not a folder")
            self.tree.pretty_print_tree()


    def add_file(self):
        folder_name = File(input("Type the name of the folder where you want to add a file: "))
        new_file_name = input("File name: ")

        parent_node = self.tree.find_node_by_name(folder_name)
        if parent_node is not None and parent_node.is_folder():
            self.tree.add_node(folder_name, new_file_name)
            print("File added successfully")
            self.tree.pretty_print_tree()
        else:
            print("Parent folder not found or it's not a folder")
            self.tree.pretty_print_tree()


    def edit_folder(self):
        old_name = input("Folder name to edit: ")
        new_name = input("Folder new name: ")
        if self.tree.rename_node(old_name, new_name):
            print("Folder renamed successfully")
            self.tree.pretty_print_tree()
        else:
            print("Folder not found")
            self.tree.pretty_print_tree()


    def edit_file(self):
        old_name = input("File name to edit: ")
        new_name = input("File new name: ")
        if self.tree.rename_node(old_name, new_name):
            print("File renamed successfully")
            self.tree.pretty_print_tree()
        else:
            print("File not found")
            self.tree.pretty_print_tree()


    def delete_folder(self):
        name = input("Folder name to delete: ")
        if self.tree.delete_node(name):
            print("Folder deleted successfully")
            self.tree.pretty_print_tree()
        else:
            print("Folder not found")
            self.tree.pretty_print_tree()


    def delete_file(self):
        name = input("File name to delete: ")
        if self.tree.delete_node(name):
            print("File deleted successfully")
            self.tree.pretty_print_tree()
        else:
            print("File not found.")
            self.tree.pretty_print_tree()

