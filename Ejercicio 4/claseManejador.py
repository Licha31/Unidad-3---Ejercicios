import numpy as np
from claseEmpleado import Empleado
from claseEmpExterno import EmpleadoExterno
from claseEmpPlanta import EmpleadoPlanta
from claseEmpContratado import EmpleadoContratado
from datetime import date
import csv

class manejaEmpleados:
    __dimension = 0
    __posicion = 0
    __arregloEmpleados = None
    __fecha = date.fromisoformat('2023-10-10')
    
    def __init__(self,dimension):
        self.__dimension = dimension
        self.__arregloEmpleados = np.empty(self.__dimension, dtype=Empleado)
        
    def agregaEmpleado(self, unEmpleado):
        self.__arregloEmpleados[self.__posicion]= unEmpleado
        self.__posicion += 1
        
    def carga(self):
        archivo1 = open('planta.csv',encoding='utf-8')
        reader = csv.reader(archivo1, delimiter=';')
        for fila in reader:
            self.agregaEmpleado(EmpleadoPlanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]))
        archivo1.close()
        archivo2 = open('externo.csv',encoding='utf-8')
        reader = csv.reader(archivo2, delimiter=';')
        for fila in reader:
            self.agregaEmpleado(EmpleadoExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9]))
        archivo2.close()
        archivo3 = open('contratado.csv',encoding='utf-8')
        reader = csv.reader(archivo3, delimiter=';')
        for fila in reader:
            self.agregaEmpleado(EmpleadoContratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7]))
        archivo3.close()
        
    #def muestraArreglo(self):
        #for empleado in self.__arregloEmpleados:
            #print(empleado)
            
            
    def sumaHoras(self,dni,horas):
        i = 0
        band = True
        verifica = None
        while (i<len(self.__arregloEmpleados) and band):
            if self.__arregloEmpleados[i].getDNI() == dni:
                band = False
                nuevasHoras = self.__arregloEmpleados[i].sumaHoraTotal(horas)
                print('Horas totales trabajadas: {}'.format(nuevasHoras))
            else:
                i = i + 1
                
    def muestraMontoObra(self, tarea):
        i = 0
        band = True
        while (i<len(self.__arregloEmpleados) and band):
            if (type(self.__arregloEmpleados[i]) == EmpleadoExterno):
                if self.__arregloEmpleados[i].getTarea() == tarea:
                    if self.__arregloEmpleados[i].getFechaFin() > self.__fecha:
                        band = False
                        montoObra = self.__arregloEmpleados[i].getMontoObra()
                        print('Costo de la obra: {}'.format(montoObra))
            else:
                i = i + 1
    
    def ayudaEconomica (self):
        for empleado in self.__arregloEmpleados:
            if empleado.getSueldo() < 2000:
                print("Nombre: {} Dni: {} Direccion: {} ".format(empleado.getNombre(), empleado.getDNI(), empleado.getDirec()))
    
    def mostrarSueldos (self):
        for empleado in self.__arregloEmpleados:
            print("Nombre: ", empleado.getNombre())
            print("Telefono: ", empleado.getTelefono()) 
            print("Sueldo: ", empleado.getSueldo())