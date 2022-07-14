from dao.conn import getConn


class client_dao():
    conn = None
    cursor = None

    def __init__(self):
        self.conn = getConn()
        self.cursor = self.conn.cursor()
        tableSql = "CREATE TABLE IF NOT EXISTS CLIENTES (id INTEGER PRIMARY KEY AUTOINCREMENT,  nombre TEXT, edad INTEGER, telefono TEXT, correo TEXT);"
        self.cursor.execute(tableSql)
        self.conn.commit()

    def getAll(self):
        sqlstr = "SELECT * from CLIENTES"
        self.cursor.execute(sqlstr)
        return self.cursor.fetchall()

    def addOne(self, nombre, edad, telefono, correo):
        sqlins = "INSERT INTO CLIENTES (nombre, edad, telefono, correo) values (?, ?, ?, ?);"
        self.cursor.execute(sqlins, (nombre, edad, telefono, correo))
        self.conn.commit()
