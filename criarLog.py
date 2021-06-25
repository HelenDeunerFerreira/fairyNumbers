def criarLog():
    logUsuarios = open("logDosUsuarios.txt", "a")
    nome = input("Informe seu nome: ")
    email = input("Informe seu email: ")
    logUsuarios.write(f"Nome: {nome} \n")
    logUsuarios.write(f"Email: {email} \n")
    logUsuarios.close()
