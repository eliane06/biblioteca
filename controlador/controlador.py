from abc import ABCMeta, abstractmethod
import ZODB
import BTrees.OOBTree
import persistent, transaction
from controlador.contexto import get_root

class Controlador:
    __metaclass__ = ABCMeta
    __objetos = None

    def crear(self, objeto):
        if not objeto:
            raise Exception("No esta permitido crear un objeto Nulo")
        self.validar_objeto(objeto)
        self.validar_insercion(objeto)
        self.get_objetos()[self.get_id_objeto(objeto)] = objeto
        transaction.commit()

    def borrar(self, objeto):
        if not objeto:
            raise Exception("No se puede borrar objeto Nulo")
        self.validar_borrado(objeto)
        del self.get_objetos()[self.get_id_objeto(objeto)]
        transaction.commit()


    def buscar(self, clave):
        if not clave in self.get_objetos().keys():
            raise Exception("No existe")
        return self.get_objetos()[clave]

    def listar_objetos(self):
        return self.get_objetos().values()

    def actualizar(self, objeto):
    	self.get_objetos()[self.get_id_objeto(objeto)] = objeto
    	transaction.commit()
 
    @abstractmethod
    def get_objetos(self):
        pass
 
    @abstractmethod
    def get_id_objeto(self):
        pass
    
    @abstractmethod
    def validar_objeto(self, objeto):
        pass

    @abstractmethod
    def validar_insercion(self, objeto):
        pass

    @abstractmethod
    def validar_eliminacion(self, objeto):
        pass

    



