class Empleado:
    __DNI = ''
    __nombre = ''
    __direc = ''
    __telefono = ''
    
    def __init__(self, dni, nom, direc, tel):
        self.__DNI = str(dni)
        self.__nombre = str(nom)
        self.__direc = str(direc)
        self.__telefono = str(tel)
    
    def getDirec(self):
        return self.__direc   
    def getTelefono(self):
        return self.__telefono    
    
    def getNombre(self):
        return self.__nombre   
        
    def getDNI(self):
        return self.__DNI