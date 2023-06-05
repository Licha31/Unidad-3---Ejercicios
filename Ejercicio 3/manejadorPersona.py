from clasePersona import Persona

class manejaPersona:
    __listaPersonas = []
    
    def __init__(self):
        self.__listaPersonas = []
        
    def agregaPersona(self,nombrePersona, direccionPersona, dniPersona):
        unaPersona = Persona(nombrePersona, direccionPersona, dniPersona)
        self.__listaPersonas.append(unaPersona)
    
        
    