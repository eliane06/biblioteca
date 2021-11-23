from controlador import cLector, cAutor, cEncargado
from controlador.cLibro import ControlLibroImpreso, ControlLibroDigital, ControladorLibro
from modelo import autor, correo, ficha, encargado, lector
from modelo.libros import LibroImpreso, LibroDigital, Literario, Cientifico
from vista import util
from datetime import date 
from modelo.ficha import Ficha
from vista.menu_entrada import menu_inicio 
 
REQUERIDO = True

def imprime(mensaje):
    print(mensaje)

def iniciar_sesion():
    global funcionario
    nombre = util.leer_cadena("Ingrese su nombre: ")
    codigo = util.leer_cadena("Ingrese su numero de codigo: ")
    try:
        funcionario = cEncargado.ControlEncargado().buscar(codigo, nombre)
        return funcionario
    except Exception as e:
        imprime(e)
        iniciar_sesion()

def cerrar_sesion():
    imprime("Cierre de Sesion exitosa")
    exit()

def registrar_lector():
    cedula = util.leer_cadena('Ingrese cédula: ', requerido=REQUERIDO)
    nombre = util.leer_cadena('Ingrese nombre: ', REQUERIDO)
    apellido = util.leer_cadena('Ingrese apellido: ', REQUERIDO)
    carnet = util.leer_cadena('Ingrese nro_carnet: ', REQUERIDO)
    ficha = Ficha()
    email = util.leer_cadena('Ingrese su direccion de email: ', REQUERIDO)
    lector1 = lector.Lector(carnet, ficha, email, nombre, apellido, cedula)
    try:
        cLector.ControlLector().crear(lector1)
        imprime("Registro guardado correctamente!")
    except Exception as ex:
        imprime(ex)

def registrar_encargado():
    nombre = util.leer_cadena('Ingrese nombre: ', REQUERIDO)
    apellido = util.leer_cadena('Ingrese apellido: ', REQUERIDO)
    cedula = util.leer_cadena('Ingrese cédula: ', REQUERIDO)
    nro = util.leer_cadena('Ingrese nro_funcionario: ', REQUERIDO)
    funcionario = encargado.Encargado(nro, nombre, apellido, cedula)
    try:
        cEncargado.ControlEncargado().crear(funcionario)
        imprime("Registro Exitoso")
    except Exception as e:
        imprime(e)        

def registrar_libros():
    nombre = util.leer_cadena('Ingrese el titulo del libro: ', REQUERIDO)
    codigo = util.leer_cadena("Ingrese el codigo del libro:", REQUERIDO)
    edicion = util.leer_cadena("Ingrese el numero de edicion:", REQUERIDO)
    autor = guardar_Autor()
    mensaje = "Ingrese 1 si es un libro Digital. En caso contrario ingrese un 0"
    literario = Literario()
    if elige_libro(mensaje): 
        formato = util.leer_cadena("Ingrese el formato del libro:", REQUERIDO)
        precio = util.leer_cadena("Ingrese el precio del libro:", REQUERIDO)
        libro = LibroDigital(formato, precio, codigo, nombre, literario, edicion, autor)
        try:
            ControlLibroDigital().crear(libro)
            imprime("Registro Exitoso")
        except Exception as e:
            imprime(e)
    else:
        libro = LibroImpreso(codigo, nombre, literario, edicion, autor)
        try:
            ControlLibroImpreso().crear(libro)
            imprime("Registro Exitoso")
        except Exception as e:
            imprime(e)
       

def elige_libro(mensaje):
    imprime(mensaje)
    valor = util.leer_entero("", 0, 1, REQUERIDO)
    return valor
    
 
def guardar_Autor():
    autor_nom = util.leer_cadena("Ingrese el nombre del Autor:")
    autor_apel = util.leer_cadena("Ingrese el apellido del Autor:")
    nacionalidad = util.leer_cadena("Ingrese la nacionalidad del Autor:")
    return autor.Autor(nacionalidad, autor_nom, autor_apel, '')
    

def prestar_libros():
    codigo = util.leer_cadena("Ingrese el codigo del libro que desee prestar: ")
    carnet = util.leer_cadena("Ingrese el numero de carnet del lector: ", REQUERIDO)
    dia = util.leer_cadena("Ingrese el dia de hoy: ", REQUERIDO)
    mes = util.leer_cadena("Ingrese el mes: ", REQUERIDO)
    anho = util.leer_cadena("Ingrese el anho: ", REQUERIDO)
    try:
        libro = ControlLibroImpreso().buscar(codigo)
        lector = cLector.ControlLector().buscar(carnet)
        fecha = ver_fecha(dia, mes, anho)
        if funcionario.prestar(libro, fecha, lector):
            imprime("El prestamo se ha realizado con exito")
            cLector.ControlLector().actualizar(lector)
            ControlLibroImpreso().actualizar(libro)
        else:
            imprime("No fue posible hacer el prestamo")
    except Exception as e:
        imprime(e)


def ver_fecha(dia, mes, anho):
    try:
        fecha = date(int(anho), int(mes), int(dia)) 
        return fecha
    except Exception as e:
        raise Exception("La fecha no es valida")
        

def devolver_libros():
    codigo = util.leer_cadena("Ingrese el codigo del libro que desee devolver: ")
    carnet = util.leer_cadena("Ingrese el numero de carnet del lector: ", REQUERIDO)
    dia = util.leer_cadena("Ingrese el dia de hoy: ", REQUERIDO)
    mes = util.leer_cadena("Ingrese el mes: ", REQUERIDO)
    anho = util.leer_cadena("Ingrese el anho: ", REQUERIDO)
    try:
        libro = ControlLibroImpreso().buscar(codigo)
        lector = cLector.ControlLector().buscar(carnet)
        cLector.ControlLector().libro_es_prestado(lector, libro)
        fecha = ver_fecha(dia, mes, anho)
        if funcionario.devolver(libro, fecha, lector):
            monto = lector.get_monto()
            imprime("Debe pagar una monto de:" + str(monto))
            cLector.ControlLector().actualizar(lector)
            ControlLibroImpreso().actualizar(libro)
        else: 
            imprime("Devolución exitosa")
    except Exception as e:
        imprime(e)


def enviar_avisos():
    lectores = cLector.ControlLector().listar_objetos()
    dia = util.leer_cadena("Ingrese el dia de hoy: ", REQUERIDO)
    mes = util.leer_cadena("Ingrese el mes: ", REQUERIDO)
    anho = util.leer_cadena("Ingrese el anho: ", REQUERIDO)
    try:
        fecha = ver_fecha(dia, mes, anho)
        for lector in lectores:
            avisado = funcionario.ver_lector(lector, fecha)
            if avisado:
                correo = correo.Correo()
                mensaje = "Su tiempo de prestamo ha pasado. Tiene hasta el dia de hoy para acercar a devolver el libro sin ser multado."
                correo.enviar(mensaje, lector.get_email())
    except Exception as e:
        imprime(e)

def reservar_libros():
    codigo = util.leer_cadena("Ingrese el codigo del libro que desee reservar: ")
    carnet = util.leer_cadena("Ingrese el numero de carnet del lector: ", REQUERIDO)
    dia = util.leer_cadena("Ingrese el dia de hoy: ", REQUERIDO)
    mes = util.leer_cadena("Ingrese el mes: ", REQUERIDO)
    anho = util.leer_cadena("Ingrese el anho: ", REQUERIDO)
    try:
        libro = ControlLibroImpreso().buscar(codigo)
        lector = cLector.ControlLector().buscar(carnet)
        fecha = ver_fecha(dia, mes, anho)
        if funcionario.reservar(libro, fecha, lector):
            print("La reserva se ha realizado con exito")
            cLector.ControlLector().actualizar(lector)
            ControlLibroImpreso().actualizar(libro)
        else:
            print("No fue posible hacer la reserva")
    except Exception as e:
        imprime(e)


def cancelar_reserva():
    codigo = util.leer_cadena("Ingrese el codigo del libro que desee cancelar su reserva: ")
    carnet = util.leer_cadena("Ingrese el numero de carnet del lector: ", REQUERIDO)
    dia = util.leer_cadena("Ingrese el dia de hoy: ", REQUERIDO)
    mes = util.leer_cadena("Ingrese el mes: ", REQUERIDO)
    anho = util.leer_cadena("Ingrese el anho: ", REQUERIDO)
    try:
        libro = ControlLibroImpreso().buscar(codigo)
        lector = cLector.ControlLector().buscar(carnet)
        fecha = ver_fecha(dia, mes, anho)
        if funcionario.reservar(libro, fecha, lector):
            print("La reserva se ha cancelado con exito")
            cLector.ControlLector().actualizar(lector)
            ControlLibroImpreso().actualizar(libro)
        else:
            print("No fue posible cancelar la reserva")
    except Exception as e:
        imprime(e)


def pagar_multa():
    carnet = util.leer_cadena("Ingrese el numero de carnet del lector: ", REQUERIDO) 
    try:
        lector = cLector.ControlLector().buscar(carnet)
        funcionario.cobrar_multa(lector)
        cLector.ControlLector().actualizar(lector)
    except Exception as e:
        imprime(e)


def vender_libros():
    codigo = util.leer_cadena("Ingrese el codigo del libro que desee comprar")
    carnet = util.leer_cadena("Ingrese el numero de carnet del lector: ", REQUERIDO)
    try:
        libro = ControlLibroDigital().buscar(codigo)
        lector = cLector.ControlLector().buscar(carnet)
        if funcionario.vender(libro):
            monto = libro.calcular_monto()
            ControlLibroDigital().actualizar(libro)
            imprime("El monto del libro es:" + " " + str(monto))
    except Exception as e:
        imprime(e)


def borrar_lector():
    carnet = util.leer_cadena("Ingrese el numero de carnet del lector: ", REQUERIDO)
    try:
        lector = cLector.ControlLector().buscar(carnet)
        cLector.ControlLector().borrar(lector)
    except Exception as e:
        imprime(e)

def borrar_libro_Impreso():
    codigo = util.leer_cadena("Ingrese el codigo del libro que desea borrar de los registros: ", REQUERIDO)
    try:
        libro = ControlLibroImpreso().buscar(codigo)
        ControlLibroImpreso().borrar(libro)
        imprime("Se ha eliminado los registros del libro")
    except Exception as e:
        imprime(e)

def borrar_libro_digital():
    codigo = util.leer_cadena("Ingrese el codigo del libro que desea borrar de los registros: ", REQUERIDO)
    try:
        libro = ControlLibroDigital().buscar(codigo)
        ControlLibroDigital().borrar(libro)
        imprime("Se ha eliminado los registros del libro")
    except Exception as e:
        imprime(e)


def listar_lector():
    lectores = cLector.ControlLector().listar_objetos()
    for lector in lectores:
        print(lector)

def listar_libros_digitales():
    libros = ControlLibroDigital().listar_objetos()
    for libro in libros:
        print(libro)

def listar_libros():
    libros = ControlLibroImpreso().listar_objetos()
    for libro in libros:
        print(libro)




