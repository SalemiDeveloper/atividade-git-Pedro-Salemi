usuarios = []
contador_id = 1

def listar_usuarios():
    print("\n📋 Lista de Usuários:")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario['id']} | Nome: {usuario['nome']} | Email: {usuario['email']}")

def adicionar_usuario():
    global contador_id
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    usuarios.append({"id": contador_id, "nome": nome, "email": email})
    print("✅ Usuário adicionado com sucesso!")
    contador_id += 1

def atualizar_usuario():
    id_alvo = int(input("Digite o ID do usuário a ser atualizado: "))
    for usuario in usuarios:
        if usuario["id"] == id_alvo:
            usuario["nome"] = input("Novo nome: ")
            usuario["email"] = input("Novo email: ")
            print("✅ Usuário atualizado com sucesso!")
            return
    print("❌ Usuário não encontrado.")

def deletar_usuario():
    id_alvo = int(input("Digite o ID do usuário a ser deletado: "))
    for usuario in usuarios:
        if usuario["id"] == id_alvo:
            usuarios.remove(usuario)
            print("✅ Usuário deletado com sucesso!")
            return
    print("❌ Usuário não encontrado.")

def menu():
    while True:
        print("\n====== MENU ======")
        print("1 - Listar usuários")
        print("2 - Adicionar usuário")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_usuarios()
        elif opcao == "2":
            adicionar_usuario()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida.")

menu()
