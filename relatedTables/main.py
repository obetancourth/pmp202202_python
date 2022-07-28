from dao import categoriasdao, subcategorias

catDao = categoriasdao.categorias_dao()
subCatDao = subcategorias.subcategorias_dao()

# catId = catDao.addOne("Padre 2", "ACT")
# subCatDao.addOne(catId, "Hijo 1", "ACT")
# subCatDao.addOne(catId, "Hijo 2", "ACT")
# subCatDao.addOne(catId, "Hijo 3", "ACT")
# subCatDao.addOne(catId, "Hijo 4", "ACT")

catId = 1

datos = subCatDao.getByCategoriaId(catId)

print(datos)
