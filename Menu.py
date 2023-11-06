import sys

class Menu:
    def __init__(self, program):
        self.program = program

    def show_menu(self):
        print()
        print("--------------------------------")
        print("""
MENU
1) Add folder
2) Add file
3) Edit folder
4) Edit file
5) Delete folder
6) Delete file""")

        self.get_menu_answer()

    def get_menu_answer(self):
        option = input("Opción: ")
        print()

        if option == "1":
            print("-----------add folder-----------")
            print()
            self.program.add_folder()
            self.show_menu()

        elif option == "2":
            print("------------add file------------")
            print()
            self.program.add_file()
            self.show_menu()

        elif option == "3":
            print("----------edit folder-----------")
            print()
            self.program.edit_folder()
            self.show_menu()

        elif option == "4":
            print("-----------edit file------------")
            print()
            self.program.edit_file()
            self.show_menu()

        elif option == "5":
            print("---------delete folder----------")
            print()
            self.program.delete_folder()
            self.show_menu()

        elif option == "6":
            print("----------delete file-----------")
            print()
            self.program.delete_file()
            self.show_menu()

        else:
            print("Opción inválida")
            self.show_menu()
