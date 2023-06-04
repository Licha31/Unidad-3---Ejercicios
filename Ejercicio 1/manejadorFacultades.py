from claseFacultad import Facultad
import csv

class manejaFacultades:
    __listaFacultades = []

    def __init__(self):
        self.__listaFacultades=[]
        
    def carga(self): #Carga facu y sus carreras, se fija el codigo y se cargan las carreras, si el codigo es distinto se carga nueva facu
        archivo=open("facultades.csv", encoding="utf-8")
        reader=csv.reader(archivo,delimiter=",")
        band = True
        i = 0
        for fila in reader:
            if band:
                f = Facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listaFacultades.append(f)
                band = False
                i = int(fila[0])
            else:
                if i == int(fila[0]):
                    self.__listaFacultades[len(self.__listaFacultades)-1].agregaCarrera(fila[1],fila[2],fila[3],fila[4],fila[5])
                else:    
                    i = int(fila[0])
                    facu=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                    self.__listaFacultades.append(facu)
                    
    def muestraFacu(self, cod): #Item 1
        i = 0
        band = True
        while (i<len(self.__listaFacultades) and band):
            if self.__listaFacultades[i].getCod() == cod:
                band = False
                print("===== Datos de la facultad ingresada =====")
                print("Nombre: {}".format (self.__listaFacultades[i].getNom()))
                print("{}".format(self.__listaFacultades[i].getCarreras()))
            else:
                i=i+1
        if (band):
                print("El codigo ingresado no corresponde a una facultad.")
                        
    def buscarCarrera(self,carrera):
        for facu in self.__listaFacultades:
            facu.buscarCarrera(carrera)