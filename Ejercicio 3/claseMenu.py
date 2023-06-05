from manejadorTaller import arregloTaller
from manejadorPersona import manejaPersona
from manejadorInscripcion import manejaInscripcion
class Menu:
    __opcion = None
    
    def mostrarMenu (self):
        tall = arregloTaller() 
        tall.carga()
        pers = manejaPersona()
        ins = manejaInscripcion()
        tall.muestraTalleres()
        Salir = True
        nombrePersona = 'Daniel'
        direccionPersona = 'Rivadavia 982, Sur'
        dniPersona = '43682255'
        tallerInscrip = 'Taller de Programación'
        while Salir:
            print("---MENU DE OPCIONES---")
            print ("\n")
            print("[1] Inscribir una persona en un taller. \n")
            print("[2] Consultar inscripción. \n")
            print("[3] Consultar inscriptos. \n")
            print("[4] Registrar pago. \n")
            print("[5] Guardar inscripciones. \n")
            print("[0] Salir del programa \n")
            self.__opcion = input("Ingrese una opcion: ")
            if self.__opcion == '0':
                print("Saliendo del programa.....")
                Salir = False
            if self.__opcion == '1':
                print("==Inscribir una persona en un taller.==")
                print("Ingrese los datos de la persona: ")
                #Aca van los input, acordarse de ponerlos una vez funcione todo.
                pers.agregaPersona(nombrePersona, direccionPersona, dniPersona)
                print("Ingrese nombre del taller a inscribirse: ")
                #Aca van los input, acordarse de ponerlos una vez funcione todo.
                tall.actualizaVacantes(tallerInscrip)
                ins.generaInscripcion()
                print("== Aspirante inscripto exitosamente")
                