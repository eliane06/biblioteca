
class Ficha:
    """Clase que representa a las fichas de los lectores"""
    def __init__(self):
        self.__list_libros = []
        self.__list_fecha_prestamo = []
        self.__list_reservas = []
        self.__list_fechas_reservas = []

    def agregar_libro_prestado(self, libro, fecha):
        self.__list_libros.append(libro)
        self.__list_fecha_prestamo.append(fecha)
        for lib in self.__list_libros:
            print(libro)

    def quitar_libro_prestado(self, libro):
        self.__list_libros.remove(libro)
        self.__list_fecha_prestamo.remove(fecha)

    def quitar_libro_reserva(self, libro):
        self.__list_reservas.remove(libro)

    def agregar_libro_reserva(self, libro, fecha):
        self.__list_reservas.append(libro)
        self.__list_fechas_reservas.append(fecha)

    def get_fecha_prestamo(self, libro):
        if libro in self.__list_libros:
            pos = self.__list_libros.index(libro)
            return self.__list_fecha_prestamo[pos]

    def get_fechas_prestamos(self):    
        return self.__list_fecha_prestamo

    def get_fecha_reserva(self, libro):
        if libro in self.__list_reservas:
            pos = self.__list_libros.index(libro)
            return self.__list_fechas_reservas[pos]

    def get_libros_prestados(self):
        return self.__list_libros
        
