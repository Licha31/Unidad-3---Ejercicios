from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldo_basico = 0
    __antiguedad = 0
    __sueldoPlanta = 0
    
    def __init__(self, dni, nombre, direccion, telefono, sueldo_basico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldo_basico = int(sueldo_basico)
        self.__antiguedad = int(antiguedad)
        
    def getSueldo(self): #Sueldo = sueldo básico+ 1% del sueldo básico*antigüedad
        self.__sueldoPlanta = (self.__sueldo_basico+(0.1*self.__sueldo_basico)*self.__antiguedad)
        return self.__sueldoPlanta 
            
    def __str__(self):
        print("Dni: {} Nombre: {} Direccion: {} Telefono: {} Sueldo: {} Antiguedad: {}".format(self.dni,self.nombre,self.direccion,self.telefono,self.__sueldo_basico,self.__antiguedad))
