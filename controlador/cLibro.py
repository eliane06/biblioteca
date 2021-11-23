from controlador.controlador import Controlador
from controlador.contexto import get_root
import ZODB
import BTrees.OOBTree
import persistent, transaction

class ControladorLibro(Controlador):

    def get_id_objeto(self, libro):
        return libro.get_codigo()

    def validar_objeto(self, libro):
        if not libro.get_codigo() or len(libro.get_codigo().strip()) == 0 :  
            raise Exception("Debe ingresar un codigo para el libro")
        
        if not libro.get_nombre() or len(libro.get_nombre().strip()) == 0:
            raise Exception("Debe ingresar un nombre para el libro")

        
    def validar_insercion(self, libro):
        if libro.get_codigo() in self.get_objetos().keys():
            raise Exception("Ya existe un libro con el numero de codigo ingresado")

    def validar_borrado(self, libro):
        if not libro.get_codigo() in self.get_objetos().keys():
            raise Exception("NO existe libro con el numero de codigo ingresado")
  
    def buscar_nombre(self, nombre):
        
        for nom in self.listar_objetos():
            if nombre.upper() == nom.get_nombre().upper():
                return nom
        raise Exception("No existe el libro registrado")
        
       
class ControlLibroDigital(ControladorLibro):
    __librosImpresos = None

    def validar_objeto(self, libro):
        ControladorLibro.validar_objeto(self, libro)
        if not libro.get_formato() or len(libro.get_formato().strip()) == 0:
            raise Exception("Debe ingresar el formato del libro")
        if not libro.get_precio() or len(libro.get_precio().strip()) == 0:
            raise Exception("Debe ingresar el precio del libro")

    def get_objetos(self):
        if not self.__librosImpresos:
            if not hasattr(get_root(), 'librosImpresos'):
                get_root().librosImpresos = BTrees.OOBTree.BTree()
            self.__librosImpresos = getattr(get_root(), 'librosImpresos')
        return self.__librosImpresos


class ControlLibroImpreso(ControladorLibro):
    __librosDigitales = None

    def get_objetos(self):
        if not self.__librosDigitales:
            if not hasattr(get_root(), 'librosDigitales'):
                get_root().librosDigitales = BTrees.OOBTree.BTree()
            self.__librosDigitales = getattr(get_root(), 'librosDigitales')
        return self.__librosDigitales

    



