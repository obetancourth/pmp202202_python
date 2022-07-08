# Script para extraer del chat las assistencias
# ==============================================
file_chat = open('./originAssistance.txt', mode='rt')
line = file_chat.readline().strip()
while line != "":
    if line.find("From") >= 0:
        from_index = line.find("From") + 5
        to_index = line.find(" to ")
        name = line[from_index: to_index]
        print(name.upper())
    else:
        if len(line) >= 13:
            account = line[1:14]
            print(account.upper().replace("D", "0"))
    line = file_chat.readline()
