from controlador.cPersona import ControladorPersona
from controlador.contexto import get_root
import ZODB
import BTrees.OOBTree

class ControlLector(ControladorPersona):
    __lectores = None

    def get_id_objeto(self, lector):
        return lector.get_carnet()

    def validar_objeto(self, lector):
        ControladorPersona.validar_objeto(self, lector)
        if not lector.get_carnet() or len(lector.get_carnet().strip()) == 0:
            raise Exception("Debe cargar numero de carnet del lector")

    def validar_insercion(self, lector):
        if lector.get_carnet() in self.get_objetos().keys():
            raise Exception("Ya existe un lector con el nro de carnet ingresado")

    def validar_borrado(self, lector):
        if not lector.get_carnet() in self.get_objetos().keys():
            raise Exception("NO existe lector con este nro de carnet")

    def get_objetos(self):
        if not self.__lectores:
            if not hasattr(get_root(), 'lectores'):
                get_root().lectores = BTrees.OOBTree.BTree()
            self.__lectores = getattr(get_root(), 'lectores')
        return self.__lectores


    def libro_es_prestado(self, lector, libro):
        if not libro in lector.get_libros_prestados():
            raise Exception("El libro no se encuentra prestado por el lector ") 

    

