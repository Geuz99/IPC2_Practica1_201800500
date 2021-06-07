class Nodo(object):
    def __init__(self, nombre=None, apellido=None, telefono=None, siguiente=None, anterior=None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.siguiente = siguiente
        self.anterior = anterior


class ListaDoblementeEnlazada(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0

    def insertar(self, nombre, apellido, telefono):
        nodo = Nodo(nombre, apellido, telefono)

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo

        self.contador += 1

    def insertar_inicio(self, nombre, apellido, telefono):
        if self.cabeza is not None:
            nodo = Nodo(nombre, apellido, telefono)
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo

            self.contador += 1

    def buscar_telefono(self, telefono):
        for d in self.iterar():
            if telefono == d:
                return True
        return False

    def dame_telefono(self, telefono):
        if self.cabeza is None:
            print("List has no element")
            return
        else:
            n = self.cabeza
            while n is not None:
                if telefono == n.telefono:
                    return True
                else:
                    n = n.siguiente

    def dame_nombre(self, telefono):
            n = self.cabeza
            while n is not None:
                if telefono == n.telefono:
                    return n.nombre
                else:
                    n = n.siguiente

    def dame_apellido(self, telefono):
            n = self.cabeza
            while n is not None:
                if telefono == n.telefono:
                    return n.apellido
                else:
                    n = n.siguiente

    def validacion_telefono(self, telefono):
        n = self.cabeza
        while n is not None:
            if telefono == n.telefono:
                return telefono
            else:
                n = n.siguiente

    def iterar(self):
        actual = self.cabeza
        while actual:
            nombre = actual.nombre
            apellido = actual.apellido
            telefono = actual.telefono
            actual = actual.siguiente
            yield nombre, apellido, telefono

    def recorrer_lista(self):
        if self.cabeza is None:
            print("List has no element")
            return
        else:
            n = self.cabeza
            while n is not None:
                print(n.nombre, " ")
                print(n.apellido, " ")
                print(n.telefono, " ")
                n = n.siguiente

    def sortList(self):
        if self.cabeza is None:
            return
        else:
            current = self.cabeza
            while current.siguiente is not None:
                # Index will point to node next to current
                index = current.siguiente
                while index is not None:
                    # If current's data is greater than index's data, swap the data of current and index
                    if ord(current.apellido) > ord(index.apellido):
                        tempNombre = current.nombre
                        tempApellido = current.apellido
                        tempTelefono = current.telefono
                        current.nombre = index.nombre
                        current.apellido = index.apellido
                        current.telefono = index.telefono
                        index.nombre = tempNombre
                        index.apellido = tempApellido
                        index.telefono = tempTelefono
                    index = index.siguiente
                current = current.siguiente
