from abc import ABCMeta, abstractmethod
import persistent

class Prestable(persistent.Persistent):
    __metaclass__ = ABCMeta
    """Clase que representa a cosas prestables"""
    def __init__(self):
        pass

    @abstractmethod
    def prestarse(self):
        pass
 
    @abstractmethod
    def devolverse(self):
        pass

class Vendible(persistent.Persistent):
    __metaclass__ = ABCMeta
    """Clase que representa a cosas vendibles"""

    def __init__(self):
        pass
  
    @abstractmethod
    def vender(self):
        pass

    @abstractmethod
    def calcular_monto(self):
        pass 

class Reservable(persistent.Persistent):
    __metaclass__ = ABCMeta
    """Clase que representa a los bienes reservables"""
    @abstractmethod
    def reservarse(self):
        pass

    @abstractmethod
    def cancelar_reservado(self):
        pass
 
class Libro:
    __metaclass__ = ABCMeta
    """Clase que representa a los libros"""

    def __init__(self, codigo, nombre, tipo, edicion, autor):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__autor = autor
        self.__tipo = tipo
        self.__edicion = edicion
        self.__estado_disponible = True

        
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_autor(self):
        return self.__autor 
 
    def get_edicion(self):
        return self.__edicion

    def esta_disponible(self):
        return self.__estado_disponible

    def __str__(self):
        self.__cad = "|Titulo: " + self.__nombre + ' | Autor: ' + self.__autor.__str__() + ' | Codigo: ' + self.__codigo + '| Disponible: '
        if self.esta_disponible():
            return self.__cad + "Si"
        else:
            return self.__cad + "No"
   

class TipoLibro(persistent.Persistent):
    """Clase que representa al tipo de libros"""
    __metaclass__ = ABCMeta
    def __init__(self):
        pass

class Cientifico(TipoLibro):
    """Clase que representa al tipo de libro cientifico"""
    def __init__(self, ciencia):
        super().__init__()
   

class Literario(TipoLibro):
    """Clase que representa al tipo de libro literario"""
    def __init__(self, tipo=None):
        super().__init__()

 
class LibroDigital(Libro, Vendible):
    """Clase que representa a libros digitales"""
    PORCENTAJE = 0.1
    def __init__(self, formato, precio, *args):
        super().__init__(*args)
        self.__formato = formato
        self.__precio = precio
      
    def vender(self):
        if self.esta_disponible():
            self._Libro__estado_disponible = False
            return True
        else:
            return False
  
    def calcular_monto(self):
        self.porcentaje_biblio = float(self.__precio) * self.PORCENTAJE
        return float(self.__precio) + float(self.porcentaje_biblio)

    def get_formato(self):
        return self.__formato

    def get_precio(self):
        return self.__precio

class LibroImpreso(Libro, Reservable, Prestable):
    """Clase que representa a los libros impresos"""
    def __init__(self, *args):
        super().__init__(*args)
        self.__reservado = False
        self.__estado_disponible = True

    def esta_reservado(self):
        return self.__reservado
     
    def prestarse(self):
        self._Libro__estado_disponible = False
      
    def devolverse(self):
        self._Libro__estado_disponible = True

    def reservarse(self):
        self.__reservado = True
        self._Libro__estado_disponible = False

    def cancelar_reservado(self):
        self.__reservado = False
        self._Libro__estado_disponible = True

