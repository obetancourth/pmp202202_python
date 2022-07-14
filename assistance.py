# Script para extraer del chat las assistencias
# ==============================================
file_chat = open('./originAssistance.txt', mode='rt')
line = file_chat.readline().strip()
lstAsistencia = list()
while line != "":
    if line.find("From") >= 0:
        from_index = line.find("From") + 5
        to_index = line.find(" to ")
        name = line[from_index: to_index]
        # print(name.upper())
    else:
        if len(line) >= 13:
            account = line[1:14]
            dictAlumno = {}
            dictAlumno["cuenta"] = account.upper().replace("D", "0")
            dictAlumno["nombre"] = name.upper()
            lstAsistencia.append(dictAlumno)
            # print(account.upper().replace("D", "0"))
    line = file_chat.readline()
for alumno in lstAsistencia:
    print(alumno)
print("-"*40)
print(lstAsistencia[6])
