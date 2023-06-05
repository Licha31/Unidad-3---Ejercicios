class inscripcion:
    __fechaInscripcion = str
    __pago = bool
    __persona = str
    __taller = str

    def __init__(self, fechaInscripcion, pago, persona, taller):
        self.__fechaInscripcion = str(fechaInscripcion)
        self.__pago = bool(pago)
        self.__persona = str(persona)
        self.__taller = str(taller)
    
    def registrar_pago(self):
        self.__pago = True

    def get_fechaInscripcion(self):
        return self.__fechaInscripcion
    
    def get_pago(self):
        return self.__pago
    
    def get_persona(self):
        return self.__persona
    
    def get_taller(self):
        return self.__taller