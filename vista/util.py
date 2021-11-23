def leer_entero(mensaje, valor_minimo=None, valor_maximo=None, requerido=False):
    """ (string, int, int, boolean) -> int
        La funcion pide al usuario que ingrese un numero en el rango dado por 
        valor_minimo y valor_maximo recibidos como parametros y en caso de que el
        campo sea requerido no retorna hasta que se ingrese un valor correcto.
    """
    
    try:
        valor = int(input(mensaje)) 
        if es_cadena(valor):
            raise TypeError
        if esta_rango(int(valor), int(valor_minimo), int(valor_maximo)):
            return valor
        else: 
            print("El entero debe estar en el rango {0} a {1}".format( valor_minimo, valor_maximo))
    except Exception as e:
        print("No se ingreso un valor valido. Vuelva a ingresar.")  
    
                  
    while requerido: 
        try:
            valor = int(input(mensaje))
            if es_cadena(valor):
                raise TypeError
        except Exception as e:
            print("No se ingreso un valor valido. Vuelva a ingresar.")  
        else:
            if esta_rango(valor, valor_minimo, valor_maximo):
                 return valor
            else: 
                 print("El entero debe estar en el rango {0} a {1}".format( valor_minimo, valor_maximo))


def leer_cadena(mensaje, requerido=False):
    """
       leer_cadena(string, boolean) -> string
       La funcion solicita que se ingrese una cadena. Si la cadena fue ingresada
       correctamente entonces la retorna, en caso de que este vacia, y si es un 
       campo requerido entonces vuelve a solicitar que se ingrese.
    """

    cad_leida = input(mensaje)
    if cad_leida == " ":
        print("No se permite el campo vacio. Vuelva a ingresar")
    else:
        return cad_leida

    while requerido:
        cad_leida = input(mensaje)
        if cad_leida == '':
            print("No se permite el campo vacio. Vuelva a ingresar")
        else:
            return cad_leida

def es_cadena(cad):
    """
    es_cadena(string) -> boolean
    Esta funcion retorna True si lo que recibe como parametro es una cadena en 
    caso contrario retorna False 
    """
    return (type(cad) == type('string'))
   
def esta_rango(valor, minimo, maximo):
    """
    esta_rango(int, int, int) -> boolean
    Esta funcion retorna True si el primer valor que recibe como parametro esta en 
    el rango de los dos sgtes valor igualmente recibidos y False en caso contrario
    """
    return minimo <= valor <= maximo
        

   
