from controlador.cPersona import ControladorPersona

class ControlAutor(ControladorPersona):
    def validar_objeto(self, autor):
        if not autor.get_nombre()  or len(autor.get_nombre().strip()) == 0:
            raise Exception("Debe cargar nombre del autor")

        if not autor.get_apellido()  or len(autor.get_apellido().strip()) == 0:
            raise Exception("Debe cargar apellido del autor")
  
        if not autor.get_nacionalidad()  or len(autor.get_nacionalidad().strip()) == 0:
            raise Exception("Debe cargar la nacionalidad del autor")
