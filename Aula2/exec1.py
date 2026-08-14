nome = input("Informe teu nome: ")
print(type(nome))
ano_nasc = int(input("Informe teu ano de nascimento: "))
print(type(ano_nasc))
ano_atual = int(input("Informe o ano atual: "))
print(type(ano_atual))

idade = (ano_atual-ano_nasc)
resultado = f"{nome} possui aproximadamente {idade} anos."
print(resultado)