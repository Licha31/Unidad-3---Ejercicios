from manejadorFacultades import manejaFacultades
class Menu:
    __opcion = None
    
    def mostrarMenu (self):
        facu = manejaFacultades() 
        facu.carga() 
        Salir = True
        while Salir:
            print("---MENU DE OPCIONES---")
            print ("\n")
            print("[1] Mostrar carreras de una facultad dado un codigo. \n")
            print("[2] Mostrar datos de una carrera ingresada por teclado. \n")
            print("[0] Salir del programa \n")
            self.__opcion = input("Ingrese una opcion: ")
            if self.__opcion == '0':
                print("Saliendo del programa.....")
                Salir = False
            if self.__opcion == '1':
                cod = int(input("Ingrese codigo de Facultad: "))
                facu.muestraFacu(cod)
            if self.__opcion == '2':
                nom = input("Ingrese nombre de carrera: ")
                facu.buscarCarrera(nom)
                