print ("Resolvendo a questão 4!")

print("Bem-vindo(a) à livraria da Bruna Lipovscek!")

lista_livro = [] #lista vazia
id_global = 0 #Variável

def cadastrar_livro(id): #Função para cadastrar livro
    global id_global
    print("----- MENU CADASTRAR LIVRO -----")
    NomeLivro = input("Digite o nome do livro: ")
    AutorLivro = input("Digite o nome do(a) autor(a): ")
    EditoraLivro = input("Digite o nome da editora: ")
    livro = {  #Dicionário
        "id": id,
        "nome": NomeLivro,
        "autor": AutorLivro,
        "editora": EditoraLivro
    }
    lista_livro.append(livro)  #Adiciona o livro ao dicionário
    print("Livro cadastrado com sucesso!")
    id_global += 1  #Incremento
    RetornarMenu = input("Deseja cadastrar mais algum livro? (S/N): ")
    if RetornarMenu.upper() == "S":
        cadastrar_livro(id_global)
    else:
        return  #Voltar ao menu principal

def consultar_livro(): #Função para consultar livros
    print("----- MENU CONSULTAR LIVRO -----")
    print("1 - Consultar todos os livros.")
    print("2 - Consultar por ID.")
    print("3 - Consultar por autor(a).")
    print("4 - Retornar ao menu principal.")
    consulta = input("Digite a opção desejada: ")
    while True:
        if consulta == "1":
            for livro in lista_livro:
                print(f"ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
            break
        elif consulta == "2":
            id_consulta = int(input("Digite o ID do livro: "))
            livro_encontrado = False #Pra confirmar se o livro foi encontrado
            for livro in lista_livro:
                if livro["id"] == id_consulta:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    livro_encontrado = True
                    break
            if not livro_encontrado:
                print("Não há livros com este ID. Tente novamente!")
            break
        elif consulta == "3":
            autor_consulta = input("Digite o nome do autor: ")
            livros_encontrados = False #Pra confirmar se o livro foi encontrado
            for livro in lista_livro:
                if livro["autor"].lower() == autor_consulta.lower(): #Maiúscula ou minúscula, tanto faz
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    livros_encontrados = True
            if not livros_encontrados:
                print("Nenhum livro encontrado para este autor!")
            break
        elif consulta == "4":
            break  #Voltar ao menu principal
        else:
            print("Por favor, digite uma opção válida!")
            continue

def remover_livro(): #Função para remover livro
    remover = int(input("Digite o ID do livro que deseja remover: "))
    livro_encontrado = False #Pra confirmar se o livro foi encontrado
    while True:
        for livro in lista_livro:
            if livro["id"] == remover:
                ConfirmRemove = input("Tem certeza que deseja remover este livro? (S/N): ").upper()
                if ConfirmRemove == "S":
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    livro_encontrado = True
                    break
                elif ConfirmRemove == "N":
                    print("Remoção cancelada!")
                    livro_encontrado = True
                    break
                else:
                    print("Não foi possível completar a operação. Tente novamente!")
                    livro_encontrado = True
                    break
        if livro_encontrado:
            break
        else:
            print("ID inválido! Nenhum livro foi encontrado com este ID. Tente novamente!")
            continue

while True: #Menu principal
    print("----- MENU PRINCIPAL -----")
    print("1 - Cadastrar livro.")
    print("2 - Consultar livro(s).")
    print("3 - Remover livro.")
    print("4 - Sair")
    OpcaoMenu = input("Digite a opção desejada: ")
    if OpcaoMenu == "1":
        id_global += 1 #incremento
        cadastrar_livro(id_global)
    elif OpcaoMenu == "2":
        consultar_livro()
    elif OpcaoMenu == "3":
        remover_livro()
    elif OpcaoMenu == "4":
        print("Agradecemos por utilizar nosso programa! Volte sempre!")
        break
    else:
        print("Opção inválida. Por favor, digite uma opção válida!")
        continue
