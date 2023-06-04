from claseCarrera import Carrera

class Facultad:
    __codigo = ''
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carreras = []
    
    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = int(codigo)
        self.__nombre = str(nombre)
        self.__direccion = str(direccion)
        self.__localidad = str(localidad)
        self.__telefono = str(telefono)
        self.__carreras=[]
        
    def agregaCarrera(self,codigo,nombre,titulo,duracion,grado):
        obj=Carrera(codigo, nombre,titulo,duracion,grado)
        self.__carreras.append(obj)
                
    def getCarreras(self):
        i = 0
        for i in range(len(self.__carreras)):
            print("Nombre de carrera: {}".format(self.__carreras[i].getNombre()))
                        
    def buscarCarrera(self,carrera):
        i = 0
        flag=False
        while not flag and i<len(self.__carreras):
            if self.__carreras[i].getNombre() == carrera:
                print(f"Codigo de Facultad:{self.__codigo},Codigo de facultad:{self.__carreras[i].getCodigo()}")
                print(self.__nombre)
                print("Localidad: ",self.__localidad)
                flag=True
            else:
                i+=1
                    
    def getCod(self):
        return self.__codigo
    def getNom(self):
        return self.__nombre
    def getDir(self):
        return self.__direccion
    def getLoc(self):
        return self.__localidad
    def getTel(self):
        return self.__telefono
    