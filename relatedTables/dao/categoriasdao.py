from dao.conn import getConn


class categorias_dao():
    conn = None
    cursor = None

    def __init__(self):
        self.conn = getConn()
        self.cursor = self.conn.cursor()
        tableSql = "CREATE TABLE IF NOT EXISTS CATEGORIAS (id INTEGER PRIMARY KEY AUTOINCREMENT,  nombre TEXT, estado TEXT);"
        self.cursor.execute(tableSql)
        self.conn.commit()

    def getAll(self):
        sqlstr = "SELECT * from CATEGORIAS"
        self.cursor.execute(sqlstr)
        rows = self.cursor.fetchall()
        oRows = list()
        for row in rows:
            oRows.append(
                {
                    "id": row[0],
                    "nombre": row[1],
                    "estado": row[2],
                }
            )
        return oRows

    def addOne(self, nombre, estado):
        sqlins = "INSERT INTO CATEGORIAS (nombre, estado) values (?, ?);"
        self.cursor.execute(sqlins, (nombre, estado))
        self.conn.commit()
        return self.cursor.lastrowid

    def getOne(self, id):
        sqlstr = "SELECT * from CATEGORIAS where id = ?;"
        self.cursor.execute(sqlstr, (id,))
        row = self.cursor.fetchone()
        return {
            "id": row[0],
            "nombre": row[1],
            "estado": row[2]
        }
