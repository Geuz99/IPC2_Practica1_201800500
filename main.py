from ListaDoble import *

datos = ListaDoblementeEnlazada()


def menu_agenda():  # MENU DE OPCIONES
    print('--------------MENU--------------')
    print('1.INGRESAR NUEVO CONTACTO.')
    print('2.BUSCAR CONTACTO.')
    print('3.VISUALIZAR AGENTA.')


def start_menu():
    opcion = -1

    while opcion != 4:
        menu_agenda()

        try:
            opcion = int(input('Elija una opción >>>>>>>>>>>> '))
        except Exception:
            print('opción no disponible')

        if opcion == 1:
            nombre = input("Ingrese nombre: \n")
            apellido = input("Ingrese apellido: \n")
            telefono = input("Ingrese numero de telefono: \n")

            if telefono == datos.validacion_telefono(telefono):
                print('El contacto ya existe.')
            else:
                datos.insertar(nombre, apellido, telefono)
                print("El contacto se ha agregado exitosamente")
                # print(datos.contador)

        if opcion == 2:
            numero = input('Ingrese el numero por buscar: \n')
            if datos.dame_telefono(numero):
                print('encontrado')
                print("Nombre: ", datos.dame_nombre(numero) + "\nApellido: ", datos.dame_apellido(numero) +
                      "\nNumero de telefono: ", numero)
            else:
                #print("no encontrado")
                print("El numero de telefono no existe.")
                agregar = input("Desea agregarlo? Si o No _")

                if agregar == "si":
                    nombre = input("Ingrese nombre: \n")
                    apellido = input("Ingrese apellido: \n")
                    telefono = input("Ingrese numero de telefono: \n")
                    if telefono == datos.validacion_telefono(telefono):
                        print('El contacto ya existe.')
                    else:
                        datos.insertar(nombre, apellido, telefono)
                        print("El contacto se ha agregado exitosamente")

        if opcion == 3:
            datos.sortList()
            #datos.recorrer_lista()
            #datos.imprimirGraphiz
            datos.generarGrafica()


start_menu()
