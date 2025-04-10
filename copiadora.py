print("Resolvendo a questão 3!")

print("Bem-vindo(a) à copiadora da Bruna Lipovscek!")  #Mensagem de boas-vindas com meu nome e sobrenome

def escolha_servico():
    while True:
        print("Qual é o tipo de serviço desejado?")
        print("DIG - digitalização.")
        print("ICO - impressão colorida.")
        print("IPB - impressão em preto e branco.")
        print("FOT - fotocópia.")
        escolha = input().upper()
        if escolha in ["DIG", "ICO", "IPB", "FOT"]: #Loop para garantir um serviço válido
            break
        else:
            print("Serviço inválido. Por favor, digite o código novamente!")
        continue #Repete o loop do tipo de servico

    if escolha == "DIG": #Atribuindo valor ao serviço
        ServicoValor = 1.10
    elif escolha == "ICO":
        ServicoValor = 1.00
    elif escolha == "IPB":
        ServicoValor = 0.40
    else:
        ServicoValor = 0.20
    return ServicoValor

def num_pagina():
    global paginas
    while True:
        QtdePagina = input("Digite o número de páginas:")
        try: #Tentando deixar a entrada somente com números
            QtdePagina = int(QtdePagina)
            if QtdePagina > 0 and QtdePagina <= 20000: #Condição para garantir número válido
                if QtdePagina < 20:
                    paginas = QtdePagina
                if QtdePagina >= 20 and QtdePagina < 200: # Calculando o desconto
                    paginas = QtdePagina - (QtdePagina * 0.15)
                elif QtdePagina >= 200 and QtdePagina < 2000:
                    paginas = QtdePagina - (QtdePagina * 0.20)
                elif QtdePagina >= 2000 and QtdePagina <= 20000:
                    paginas = QtdePagina - (QtdePagina * 0.25)
            elif QtdePagina > 20000:
                print("Nosso limite é de 20.000 cópias. Por favor, digite um número de cópias igual ou inferior ao limite máximo!")
                continue
            else:
                print("Por favor, digite um número válido!")
                continue
        except ValueError:
            print("Por favor, digite um número válido!") #Pára o loop de checagem de número válido
        return paginas

def servico_extra():
    while True:
            print("Deseja contratar um serviço adicional?")
            print("1 - Encadernação simples - R$15.00")
            print("2 - Encadernação capa dura - R$40.00")
            print("0 - Não desejo serviço adicional.")
            servico_extra = input() #Calculando o serviço adicional
            if servico_extra == "1":
                extraser = 15
            elif servico_extra == "2":
                extraser = 40
            elif servico_extra == "0":
                extraser = 0
            else:
                print("Por favor, digite uma opção válida!")
                continue
            return extraser

servico = escolha_servico()
num_pagina = num_pagina()
extra = servico_extra()

Total = (servico * num_pagina) + extra

print(f"Total: R${Total:.2f} (serviço: R${servico:.2f} * páginas: {int(num_pagina)} + extra: R${extra:.2f})")