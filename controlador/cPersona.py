from controlador.controlador import Controlador
from controlador.contexto import get_root

class ControladorPersona(Controlador):
    __personas = None

    def validar_objeto(self, persona):
        if not persona.get_cedula() or len(persona.get_cedula().strip()) == 0:
            raise Exception("Debe cargar cédula de la persona!")

        if not persona.get_nombre()  or len(persona.get_nombre().strip()) == 0:
            raise Exception("Debe cargar nombre de la persona!")

        if not persona.get_apellido()  or len(persona.get_apellido().strip()) == 0:
            raise Exception("Debe cargar apellido de la persona!")

    

    
     
  

   






