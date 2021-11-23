import persistent

class Persona(persistent.Persistent):
    """Clase que representa a las personas  """ 
  
    def __init__(self, nombre, apellido, cedula):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_cedula(self):
        return self.__cedula

    def __str__(self):
        return self.__nombre + ' '+ self.__apellido + ' ' + self.__cedula




