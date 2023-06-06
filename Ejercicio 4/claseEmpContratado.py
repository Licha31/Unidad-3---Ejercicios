from claseEmpleado import Empleado
from datetime import date
class EmpleadoContratado(Empleado):
    __fechaInicio = ''
    __fecha_fin = ''
    __horas_trabajadas = 0
    __valor_hora = 0
    __sueldoContratado = 0
    
    
    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas_trabajadas, valor_hora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = date.fromisoformat(fecha_inicio)
        self.__fecha_fin = date.fromisoformat(fecha_fin)
        self.__horas_trabajadas = int(horas_trabajadas)
        self.__valor_hora = float(valor_hora)
    
    def getSueldo(self): #Sueldo = cantidad de horas trabajadas * valor de la hora
        self.__sueldoContratado = (self.__horas_trabajadas * self.__valor_hora)
        return self.__sueldoContratado
        
    def getHoras(self):
        return self.__horas_trabajadas
    
    def sumaHoraTotal(self,horas):
        self.__horas_trabajadas = self.__horas_trabajadas + horas
        return self.__horas_trabajadas