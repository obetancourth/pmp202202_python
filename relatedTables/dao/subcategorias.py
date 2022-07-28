from dao.conn import getConn


class subcategorias_dao():
    conn = None
    cursor = None

    def __init__(self):
        self.conn = getConn()
        self.cursor = self.conn.cursor()
        tableSql = "CREATE TABLE IF NOT EXISTS SUBCATEGORIAS (id INTEGER PRIMARY KEY AUTOINCREMENT, categoriaId INTEGER,  nombre TEXT, estado TEXT, FOREIGN KEY(categoriaId) REFERENCES CATEGORIAS(id));"
        self.cursor.execute(tableSql)
        self.conn.commit()

    def getAll(self):
        sqlstr = "SELECT * from SUBCATEGORIAS"
        self.cursor.execute(sqlstr)
        rows = self.cursor.fetchall()
        oRows = list()
        for row in rows:
            oRows.append(
                {
                    "id": row[0],
                    "categoriaId": row[1],
                    "nombre": row[2],
                    "estado": row[3]
                }
            )
        return oRows

    def addOne(self, categoriaId, nombre, estado):
        sqlins = "INSERT INTO SUBCATEGORIAS (categoriaId, nombre, estado) values (?, ?, ?);"
        self.cursor.execute(sqlins, (categoriaId, nombre, estado))
        self.conn.commit()

    def getOne(self, id):
        sqlstr = "SELECT * from SUBCATEGORIAS where id = ?;"
        self.cursor.execute(sqlstr, (id,))
        row = self.cursor.fetchone()
        return {
            "id": row[0],
            "categoriaId": row[1],
            "nombre": row[2],
            "estado": row[3]
        }

    def getByCategoriaId(self, categoriaId):
        sqlstr = "SELECT a.id, a.categoriaId, a.nombre, a.estado, b.nombre as categoriaNombre from SUBCATEGORIAS a INNER JOIN CATEGORIAS b on a.categoriaId = b.id where a.categoriaId=?"
        self.cursor.execute(sqlstr, (categoriaId,))
        rows = self.cursor.fetchall()
        oRows = list()
        for row in rows:
            oRows.append(
                {
                    "id": row[0],
                    "categoriaId": row[1],
                    "nombre": row[2],
                    "estado": row[3],
                    "categoria": row[4],
                }
            )
        return oRows
