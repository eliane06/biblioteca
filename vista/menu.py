from vista import funciones, util

def menu():
    menus = {}
    menus[1] = {"titulo":"Prestar Libro", "funcion":funciones.prestar_libros}
    menus[2] = {"titulo":"Devolver Libro", "funcion":funciones.devolver_libros}
    menus[3] = {"titulo":"Reservar Libro", "funcion":funciones.reservar_libros}
    menus[4] = {"titulo":"Cancelar reserva", "funcion":funciones.cancelar_reserva}
    menus[5] = {"titulo":"Cobrar multa", "funcion":funciones.pagar_multa}
    menus[6] = {"titulo":"Comprar Libro", "funcion":funciones.vender_libros}
    menus[7] = {"titulo":"Enviar avisos a lectores morosos", "funcion":funciones.enviar_avisos}
    menus[8] = {"titulo":"Registrar Libro", "funcion":funciones.registrar_libros}
    menus[9] = {"titulo":"Registrar Lector", "funcion":funciones.registrar_lector}
    menus[10] = {"titulo":"Registrar Funcionario", "funcion":funciones.registrar_encargado}
    menus[11] = {"titulo":"Borrar registros de Lector", "funcion":funciones.borrar_lector}
    menus[12] = {"titulo":"Borrar registros de un libro", "funcion":funciones.borrar_libro_Impreso}
    menus[13] = {"titulo":"Borrar registros de libro digital", "funcion":funciones.borrar_libro_digital}
    menus[14] = {"titulo":"Listar Lectores", "funcion":funciones.listar_lector}
    menus[15] = {"titulo":"Listar Libros", "funcion":funciones.listar_libros}
    menus[16] = {"titulo":"Listar Libros Digitales", "funcion":funciones.listar_libros_digitales}
    menus[17] = {"titulo":"Cerrar Sesión", "funcion":funciones.cerrar_sesion}
    
    REQUERIDO = True
    while True:
        print("-----------------------------------------------------------") 
        for clave in menus.keys():
            print("{}- {}".format(clave, menus[clave]["titulo"]))
        print("-----------------------------------------------------------")
        opcion = util.leer_entero("Ingrese una opción: ", 1, 17, REQUERIDO) 
        menus[opcion]["funcion"]() 


