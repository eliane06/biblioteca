from controlador.cPersona import ControladorPersona
from controlador.contexto import get_root
import ZODB
import BTrees.OOBTree
import persistent, transaction
from controlador.contexto import get_root


class ControlEncargado(ControladorPersona):
    __funcionarios = None

    def get_id_objeto(self, encargado):
        return encargado.get_nro_funcionario()

    def buscar(self, clave, nombre):
        if not clave in self.get_objetos().keys():
            raise Exception("No existe un funcionario que posea ese codigo")
        if not self.get_objetos()[clave].get_nombre().upper() == nombre.upper():
            raise Exception("No existe un funcionario con ese nombre que tenga el codigo ingresado")
        return self.get_objetos()[clave]


    def validar_objeto(self, encargado):
        ControladorPersona.validar_objeto(self, encargado)
        if not encargado.get_nro_funcionario() or len(encargado.get_nro_funcionario().strip()) == 0:
            raise Exception("Debe cargar numero de funcionario del funcionario")

    def validar_insercion(self, encargado):
        if encargado.get_nro_funcionario() in self.get_objetos().keys():
            raise Exception("Ya existe un funcionario con el nro de identificacion ingresado")

    def validar_eliminacion(self, encargado):
        if not encargado.get_carnet() in self.get_objetos().keys():
            raise Exception("NO existe encargado con este nro de funcionario")


    def get_objetos(self):
        if not self.__funcionarios:
            if not hasattr(get_root(), 'funcionarios'):
                get_root().funcionarios = BTrees.OOBTree.BTree()
            self.__funcionarios = getattr(get_root(), 'funcionarios')
        return self.__funcionarios

  


