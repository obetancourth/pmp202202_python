import json
from bottle import route, run, response, post, request

from dao.clientedao import client_dao

holaMundoJSON = {"mensaje": "Hola Mundo"}
clientedao = client_dao()


@route('/')
def index():
    return '<h1 style="background-color:#000;color:#009900;">Hola Mundo</h1>'


@route('/json')
def json_handler():
    response.content_type = "application/json"
    return json.dumps(holaMundoJSON)


@route('/json/<id>')
def get_json_by_id_handler(id):
    response.content_type = "application/json"
    return json.dumps({"mensaje": "Llamada con parametro", "id": id})


@route('/cuenta/<cuenta>')
def getcuenta(cuenta):
    response.content_type = "application/json"
    return json.dumps({"cuenta": cuenta})


@route('/cliente/all')
def getAllClientes():
    clientes = clientedao.getAll()
    response.content_type = "application/json"
    return json.dumps(clientes)


@post('/cliente/new')
def postNewCliente():
    nombre = request.forms.get("nombre")
    edad = int(request.forms.get("edad"))
    telefono = request.forms.get("telefono")
    correo = request.forms.get("correo")
    clientedao.addOne(nombre, edad, telefono, correo)
    return json.dumps({"msg": "ok"})


@route('/cliente/byid/<id>')
def getClienteByID(id):
    cliente = clientedao.getOne(int(id))
    return json.dumps(cliente)


# http://localhost:8080/alumno/0801198412349


# {"cuenta": "0801198412349"}
# http://localhost:8080/
run(host="localhost", port=8080)
