from modelo.persona import Persona

class Lector(Persona):
    """Clase que representa a los lectores"""

    MAX_LIBRO = 3
    MAX_RESERVA = 2
    def __init__(self, nro_carnet, ficha, email, *args):
        super().__init__(*args)
        self.__nro_carnet = nro_carnet 
        self.__email = email
        self.__estado_moroso = False
        self.__ficha = ficha
        self.__cant_libros = 0
        self.__cant_reservados = 0
    
    def get_carnet(self):
        return self.__nro_carnet
   
    def get_email(self):
        return self.__email

    def puede_prestar(self):
        return not self.MAX_LIBRO == self.__cant_libros and not self.__estado_moroso
      
    def get_monto(self):
        return self.__monto_pagar
 
    def puede_reservar(self):
        return not MAX_RESERVA == self.__cant_reservados and not self.__estado_moroso
    
    def get_fechas_prestamos(self):
        return self.__ficha.get_fechas_prestamos()

    def get_dias_prestados(self, fecha, libro):
        return (fecha - self.__ficha.get_fecha_prestamo(libro)).days
   
    def get_libros_prestados(self):
        return self.__ficha.get_libros_prestados()

    def prestar(self, libro, fecha):
        self.__cant_libros += 1
        self.__ficha.agregar_libro_prestado(libro, fecha)

    def devolver(self, libro):
        self.__ficha.quitar_libro_prestado(libro, fecha)
        self.__cant_libros -= 1
            
    def reservar(self, libro, fecha):
        self.__ficha.agregar_libro_reserva(libro, fecha)
        self.__cant_reservados += 1
   
    def cancelar_reserva(self, libro):
        self.__ficha.quitar_libro_reserva(libro)
        self.__cant_reservados -= 1

    def multar(self, monto):
        self.__monto_pagar = monto
        self.__estado_moroso = True
  
    def pagar_multa(self):
        self.__monto_pagar = 0
        self.__estado_moroso = False
    
    def get_ficha(self):
        return self.__ficha

    def __str__(self):
        return '| ' + self.__nro_carnet  + ' | ' + super().__str__() + " | " + "Estado moroso: " + str(self.__estado_moroso) + "|Prestados: " + str(self.__cant_libros) + ' |Reservados: ' + str(self.__cant_reservados)
