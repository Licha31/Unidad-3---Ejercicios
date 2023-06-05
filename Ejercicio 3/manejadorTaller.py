from claseTaller import TallerCapacitacion
import numpy as np
import csv 

class arregloTaller:
    __dimension = 0
    __posicion = 0
    
    def __init__(self):
        archivo = open('datosTalleres.csv')
        reader = csv.reader(archivo, delimiter=';')
        self.__dimension = int(next(reader)[0])
        self.__arregloTalleres = np.empty(self.__dimension, dtype=TallerCapacitacion)
        archivo.close()
    
    def agregaTaller(self, unTaller):
        self.__arregloTalleres[self.__posicion]=unTaller
        self.__posicion += 1 

    def carga(self):
        archivo = open('datosTalleres.csv',encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            self.agregaTaller(TallerCapacitacion(fila[0],fila[1],fila[2],fila[3]))
    
    def muestraTalleres(self):
        i = 0
        for i in range(len(self.__arregloTalleres)):
            print("Nombre del taller {}, vacantes {}, monto de inscripcion {}".format(self.__arregloTalleres[i].get_nombre(),self.__arregloTalleres[i].get_vacantes(),self.__arregloTalleres[i].get_montoInscripcion()))
    
    def actualizaVacantes(self,tallerInscripto):
        i = 10
        band = True
        while (i<len(self.__arregloTalleres) and band):
            if tallerInscripto == self.__arregloTaller[i].get_nombre():
                band = False
                self.__arregloTalleres[i].actualizar_vacantes(1)
            else:
                i = i+1