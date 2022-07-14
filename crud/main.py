from cliente import Cliente
from ui import ui
from dao.clientedao import client_dao
ux = ui()
_cliente_dao = client_dao()
# lstClientes = list()
# for i in range(1, 51):
#     lstClientes.append(
#         Cliente("Nombre " + str(i), 50 + (i * 4))
#     )
# for cliente in lstClientes:
#     print(cliente.to_string())
opcion = 'M'
while(opcion != 'S'):
    if (opcion == 'C'):
        ux.separador()
        print("Agregando Nuevo Cliente")
        ux.separador()
        newCliente = ux.inputCliente(Cliente("", 0, "", ""))
        _cliente_dao.addOne(
            newCliente.nombre,
            newCliente.edad,
            newCliente.telefono,
            newCliente.correo
        )
    elif (opcion == 'R'):
        print("Mostrar Detalle Seleccionado")
    elif (opcion == 'U'):
        print("Editar Seleccionado")
    elif (opcion == 'D'):
        print("Eliminar Seleccionado")
    elif (opcion == 'M'):
        ux.mostrarCliente(_cliente_dao.getAll())
    else:
        print("No existe opción")
    opcion = ux.menu().rstrip().lstrip().upper()
