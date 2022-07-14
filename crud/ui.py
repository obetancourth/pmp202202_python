from cliente import Cliente


class ui:
    def separador(self):
        print("=" * 60)

    def menu(self):
        self.separador()
        print("Opciones")
        self.separador()
        print("M\tMostrar Registros")
        print("C\tNuevo Cliente")
        print("R\tVer detalle de Cliente")
        print("U\tActualizar Cliente")
        print("D\tEliminar Cliente")
        print("S\tSalir")
        self.separador()
        return input("Escriba una opción y presione Enter ")

    def inputCliente(self, cliente):
        if cliente.id != 0:
            print("Codigo:\t" + str(cliente.id))
        cliente.nombre = input("Nombre:\t")
        cliente.edad = int(input("Edad:\t"))
        cliente.telefono = input("Teléfono:\t")
        cliente.correo = input("Correo:\t")
        return cliente

    def getClienteId(self):
        id = int(input("Código:\t"))
        return id

    def mostrarCliente(self, clientes):
        self.separador()
        print("Codigo", "Nombre", "Correo", sep="\t")
        self.separador()
        for clt in clientes:
            print(clt[0], clt[1], clt[4], sep="\t")
