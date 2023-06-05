class TallerCapacitacion:
    __idTaller = 0
    __nombre = ''
    __vacantes= 0
    __montoInscripcion = 0
    
    def __init__(self, idTaller, nombre, vacantes, montoInscripcion):
        self.__idTaller = int(idTaller)
        self.__nombre = str(nombre)
        self.__vacantes = int(vacantes)
        self.__montoInscripcion = int(montoInscripcion)

    def actualizar_vacantes(self, cantidad):
        self.__vacantes -= cantidad

    def get_idTaller(self):
        return self.__idTaller
    
    def get_nombre(self):
        return self.__nombre
    
    def get_vacantes(self):
        return self.__vacantes
    
    def get_montoInscripcion(self):
        return self.__montoInscripcion