
def accion(accion):
    """"Se encarga de dado un numero de lectores, se pueda desplegar la lista de los mismos, verificar quienes estan en estado moroso y que los lectores realicen los prestamos y devolucion de libros"""
    def despliega(lectores):
         print("--------------Listando todos los lectores-------------")
         for lector in lectores.items():
             print (lector)


    def listar_morosos(lectores):
         print("--------------Lectores en estado moroso-------------")
         print([lectores[clave] for clave in lectores.keys() if lectores[clave]['Moroso '] in ['si', 'Si', 'SI']])


    def agregar_lectores(lectores=None):
        lectores[input('Carnet ')] = {y: input(y) for y in ["Cedula ", "Nombre ", "Apellido ", "Moroso "]}


    def prestar(carnet, lectores):
        if carnet in lectores.keys() and not lectores[carnet]['Moroso '] in ['si', 'Si', 'SI', 'sI']:
            leer_libro(lectores, carnet)
        else:
            print("El Lector no puede hacer el prestamo.")


    def leer_libro(lectores, carnet):
        if not "Ficha " in lectores[carnet].keys():
            lectores[carnet]["Ficha "] = [[input(y) for y in ['Titulo del Libro: ', 'Fecha: '] for x in range (1)]]
        else:
            lectores[carnet]["Ficha "].append([input(y) for y in ['Titulo del Libro: ', 'Fecha: '] for x in range (1)])


    def devolver(carnet, libro, lectores):
        if "Ficha " in lectores[carnet]:
             if sacar_libro_prestado(lectores[carnet]["Ficha "], libro, len(lectores[carnet]["Ficha "])):
                  print("El lector con numero de carnet {} no ha hecho prestamo del libro {}".format(carnet, libro))
 

    def sacar_libro_prestado(lista, libro, x):
        if x > 0 and len(lista) : 
            if libro == lista[x-1][0]:
                del lista[x-1]
                return True
            else:
                sacar_libro_prestado(lista, libro, x-1)


    acciones = {"Desplegar": despliega, "Morosos": listar_morosos, "Prestar": prestar, "Devolver": devolver, "Agregar Lectores": agregar_lectores}
    return acciones[accion]


data ={input('Carnet ') : {y: input(y) for y in ["Cedula ", "Nombre ", "Apellido ", "Moroso "]} for x in range(1)}

a = accion('Desplegar')
a(data)
a = accion('Morosos')
a(data)
a = accion("Prestar")
a('123', data)
a = accion("Prestar")
a('123', data)
a = accion('Desplegar')
a(data)
a = accion("Devolver")
a('123', 'Libro2', data)
a = accion('Desplegar')
a(data)
a = accion("Agregar Lectores")
a(data)
a = accion('Desplegar')
a(data)

