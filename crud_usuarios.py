usuarios = []
contador_id = 1

def listar():
    for usuario in usuarios:
        print(f"{usuario['id']} - {usuario['nome']} ({usuario['email']})")

def adicionar():
    global contador_id
    nome = input("Nome: ")
    email = input("Email: ")
    usuarios.append({"id": contador_id, "nome": nome, "email": email})
    contador_id += 1

def atualizar():
    id_usuario = int(input("ID para atualizar: "))
    for u in usuarios:
        if u["id"] == id_usuario:
            u["nome"] = input("Novo nome: ")
            u["email"] = input("Novo email: ")

def menu():
    while True:
        print("\n1 - Listar\n2 - Adicionar\n3 - Atualizar\n4 - Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            listar()
        elif opcao == "2":
            adicionar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            break

menu()
