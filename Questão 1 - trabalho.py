print ("Resolvendo a questão 1!")

print ("Bem-vindo(a) à loja da Bruna Lipovscek!") #Exibindo uma mensagem de boas-vindas com meu nome

ValorUnitario = float(input("Digite o valor do produto:")) #Implementando os input
Quantidade = int(input("Digite a quantidade do produto:"))

if ValorUnitario <= 0:
    print("O valor do produto precisa ser maior que zero.") #Achei legal add que o valor precisa ser maior que zero

ValorTotal = ValorUnitario * Quantidade

if ValorTotal < 2500:
    desconto = 0
elif 2500 >= ValorTotal < 6000:    #Utilizando if, elif e else
    desconto = 4
elif 6000 >= ValorTotal < 10000:
    desconto = 7
else:
    desconto = 11

DescontoTotal = ValorTotal * (desconto / 100) #Calculando a porcentagem

ValorTotalComDesconto = ValorTotal - DescontoTotal

print (f"O valor sem desconto é R${ValorTotal}0") #Apresentando valores com e sem desconto

print (f"O valor com desconto é R${ValorTotalComDesconto}0")