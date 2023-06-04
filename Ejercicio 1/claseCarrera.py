class Carrera:
    __codigo = ''
    __nombre = ''
    __titulo = ''
    __duracion = ''
    __grado = ''

    def __init__(self,codigo,nombre,titulo,duracion,grado):
        self.__codigo= int(codigo)
        self.__nombre= str(nombre)
        self.__titulo= str(titulo)
        self.__duracion= str(duracion)
        self.__grado= str(grado)
        
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre

    def getDuracion(self):
        return self.__duracion
    
    def getTitulo(self):
        return self.__titulo
    
    def getGrado(self):
        return self.__grado