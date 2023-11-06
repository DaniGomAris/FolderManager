import sys

class Menu:
    def __init__(self, program):
        self.program = program

    def show_menu(self):
        print()
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
        print()

        if option == "1":
            print()
            self.program.add_folder()
            self.show_menu()

        elif option == "2":
            print()
            self.program.add_file()
            self.show_menu()

        elif option == "3":
            print()
            self.program.edit_folder()
            self.show_menu()

        elif option == "4":
            print()
            self.program.edit_file()
            self.show_menu()

        elif option == "5":
            print()
            self.program.delete_folder()
            self.show_menu()

        elif option == "6":
            print()
            self.program.delete_file()
            self.show_menu()

        elif option == "7":
            print()
            sys.exit("Adios")
        else:
            print("Opción inválida")
            self.show_menu()
