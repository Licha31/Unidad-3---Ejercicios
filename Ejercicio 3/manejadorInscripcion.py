from claseInscripcion import inscripcion
import numpy as np

class manejaInscripcion:
    __dimension = 0
    __incremento = 5
    __cantidad = 0

    def __init__(self, dimension=5):
        self.__registroInscrip = np.empty(dimension, dtype=inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        
    def generaInscripcion(self, registroInscrip):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__cantidad
            self.__registroInscrip.resize(self.__dimension, refcheck=False)
        self.__registroInscrip[self.__cantidad] = registroInscrip() 
        self.__cantidad += 1 