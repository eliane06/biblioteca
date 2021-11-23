#falto colocar este..

def menu_inicio():
    menus = {}
    menus[1] = {"titulo":"Registrarse", "funcion":funciones.registrar_encargado}
    menus[2] = {"titulo":"Iniciar Secion", "funcion":funciones.iniciar_sesion}
    menus[3] = {"titulo":"Salir", "funcion":funciones.cerrar_sesion}
 
    REQUERIDO = True
    while True:
        print("-----------------------------------------------------------") 
        for clave in menus.keys():
            print("{}- {}".format(clave, menus[clave]["titulo"]))
        print("-----------------------------------------------------------")
        opcion = util.leer_entero("Ingrese una opcion: ", 1, 3 , REQUERIDO) 
        menus[opcion]["funcion"]() 
