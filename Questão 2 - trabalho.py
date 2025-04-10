print("Resolvendo a questão 2!")

print("Bem-vindo(a) à açaíteria da Bruna Lipovscek!")  #Mensagem de boas-vindas com meu nome e sobrenome

print("--------------------- Cardápio ---------------------")
print("--| Tamanho | --| Açaí (AC) |-- --| Cupuaçu (CP) |--")
print("--|    P    | --|  R$11.00  |-- --|     R$9.00   |--")
print("--|    M    | --|  R$16.00  |-- --|    R$14.00   |--")
print("--|    G    | --|  R$20.00  |-- --|    R$18.00   |--")

TotalPedido = 0  #Variável para acumular o valor total do pedido

while True:  #Loop principal do pedido

    while True:  #Loop para garantir um sabor válido
        Sabor = input("Digite o sabor desejado (AC ou CP):")
        if Sabor in ["AC", "CP"]:
            break
        print("Sabor inválido. Tente novamente!")
        continue  #Pula para o início do loop de sabor

    while True:  #Loop para garantir um tamanho válido
        Tamanho = input("Digite o tamanho desejado (P, M ou G):")
        if Tamanho in ["P", "M", "G"]:
            break
        print("Tamanho inválido. Tente novamente!")
        continue  #Pula para o início do loop de tamanho

    if Sabor == "AC":  #Estrutura aninhada para determinar nome e preço
        NomeDoSabor = "açaí"
        if Tamanho == "P":
            Valor = 11
        elif Tamanho == "M":
            Valor = 16
        else:
            Valor = 20
    else:  #Caso o sabor seja CP
        NomeDoSabor = "cupuaçu"
        if Tamanho == "P":
            Valor = 9
        elif Tamanho == "M":
            Valor = 14
        else:
            Valor = 18

    TotalPedido = TotalPedido + Valor  #Acumulando o valor total

    print(f"Você pediu um {NomeDoSabor} tamanho {Tamanho}: R${Valor}.00")

    while True:  #Loop para garantir uma resposta válida sobre pedir mais alguma coisa
        MaisAlgumaCoisa = input("Deseja pedir mais alguma coisa? (S/N):")
        if MaisAlgumaCoisa in ["S", "N"]:
            break
        print("Resposta inválida. Digite S para sim ou N para não!")
        continue  #Pula para o início do loop sobre pedir mais alguma coisa

    if MaisAlgumaCoisa == "N":
        print(f"Total do pedido: R${TotalPedido}.00")
        break  #Finalizando o loop principal