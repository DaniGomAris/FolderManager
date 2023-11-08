class File:
    def __init__(self, name, size, creation_date):
        self.name = name
        self.size = size  # Tamaño en bytes
        self.creation_date = creation_date
        

class Folder:
    def __init__(self, name, size, creation_date):
        self.name = name
        self.size = size # Tamaño en bytes
        self.creation_date = creation_date
    