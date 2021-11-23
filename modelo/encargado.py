from modelo.persona import Persona

class Encargado(Persona):
    """Clase que representa a los encargados o funcionarios de la biblioteca"""
    
    MAX_DIAS = 10 #cantidad de dias que puede durar un prestamo de un libro
    CONSIDERACION = 1 #dias de consideracion para no multar
    MULTA_DIARIA = 5000

    def __init__(self, nro_funcionario, *args):
        super().__init__(*args)
        self.__nro_funcionario = nro_funcionario

    def get_nro_funcionario(self):
        return self.__nro_funcionario
    
    def prestar(self, libro, fecha, lector):
        if libro.esta_disponible() and lector.puede_prestar() and not libro.esta_reservado():
            libro.prestarse() 
            lector.prestar(libro, fecha)
            return True
        else:
            return False

    def devolver(self, libro, fecha, lector):
        libro.devolverse()
        cant_dias_prestados =  lector.get_dias_prestados(fecha, libro)
        if cant_dias_prestados > self.MAX_DIAS + self.CONSIDERACION:
            dias = cant_dias_prestados - (self.MAX_DIAS + self.CONSIDERACION)
            lector.multar(dias * self.MULTA_DIARIA)
            return True
        return False

    def ver_lector(self, lector, fecha_actual):
        for fecha in lector.get_fechas_prestamos():
            if (fecha_actual - fecha).days == self.MAX_DIAS + self.CONSIDERACION:
                return True
        return False

    def reservar(self, libro, fecha, lector):
        if libro.esta_disponible() and lector.puede_reservar and not libro.esta_reservado:
            libro.reservarse()
            lector.reservar(libro, fecha)
            return True
        return False

    def cancelar_reserva(self, libro, lector):
        if libro.esta_reservado:
            libro.cancelar_reservado()
            lector.cancelar_reserva(libro)
            return True
        else:
            return False

    def cobrar_multa(self, lector):
        lector.pagar_multa()

    def vender(self, libro):
        if libro.vender():
           return True
        else:
           return False

