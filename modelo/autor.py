from modelo.persona import Persona

class Autor(Persona):
    """ Clase que representa a autores """

    def __init__(self, nacionalidad, *args):
        super().__init__(*args)
        self.__nacionalidad = nacionalidad

    def __str__(self):
        return super().__str__() + self.__nacionalidad
