#Exemplo 1
cont = 1
while True:
    if cont == 5:
        break
    else:
        print("Infinito")
        cont += 1
        continue

#Exemplo 2

senha_correta = "123"
senha = input("Digite a sua senha: ")
for x in range (1, 4):
    if senha == senha_correta:
        print("Senha Correta, Acesso Permitido!")
        break
    else:
        print(f"Senha Incorreta {x} tentativa")
        senha = input("Digite a sua senha: ")
        if x == 3:
            print("Acesso Negado!")
        continue

#Exemplo 3
print("Sistema de Vendas")

qtd_itens = int(input("Informe quantos itens: "))
total_geral_compra: float = 0.0
produto_mais_caro: float = 0.0
lista_valores: list = []
lista_produto: list = []
print(qtd_itens)

for cont in range (1, qtd_itens + 1):
    qtd_total_produto = 0
    total_produto = 0.0
    print(f"\nProduto {cont}: ")
    nome = input("Informe o nome do produto: ")
    valor = float(input("Informe o valor do produto: R$"))
    qtd_total_produto = int(input("Informe quantos itens de produto: "))
    total_produto = valor * qtd_total_produto
    produto = (nome, valor, qtd_total_produto, total_produto)
    lista_produto.append(tuple(produto))
    lista_valores.append(valor)
    total_geral_compra += total_produto

produto_mais_caro = max(lista_valores)
for produto in lista_produto:
    print(f"Nome: {produto[0]}")
    print(f"Valor: R${produto[1]}")
    print(f"Quantidade Total: {produto[2]}")
    print(f"Valor Total: R${produto[3]}")

print(f"\nO produto mais caro é o valor de: R${produto_mais_caro}")