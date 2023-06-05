class Persona:
    __nombre = str
    __direccion = str
    __dni = int
    
    def __init__(self, nombre, direccion, dni):
        self.__nombre = str(nombre)
        self.__direccion = str(direccion)
        self.__dni = int(dni)

    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_dni(self):
        return self.__dni