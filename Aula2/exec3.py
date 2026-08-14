# Questao 1

num = float(input("Digite o numero: "))
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Zero")

# Questao 2

num = float(input("Digite um numero: "))
if num %2 == 0:
    print("Par")
else:
    print("Impar")

# Questao 3

num1 = float(input("Digite o 1º numero: "))
num2 = float(input("Digite o 2º numero: "))
if num1 > num2:
    print(f"O maior numero é {num1}")
elif num2 > num1:
    print(f"O maior numero é {num2}")
else:
    print("Os numeros são iguais")

# Questao 4
'''FEITO POR MIM'''

salario = float(input("Digite o seu salario: "))
if salario <= 2000:
    salario_aumentado = ((10 / 100) * salario) + salario
    print(f"O salario aumentará em 10% e o novo salario será: {salario_aumentado}")
else:
    salario_aumentado = ((5 / 100) * salario) + salario
    print(f"O salario aumentará em 5% e o novo salario será: {salario_aumentado}")

'''FEITO POR RENAN'''

salario = float(input("Informe o seu salario: "))
percentual = 5
valor_aumento = salario * 0.05

if salario <= 2000:
    percentual = 10
    valor_aumento = salario * 0.1

salario_final = valor_aumento + salario

print(f"Aumento de: {percentual}%")
print(f"Valor do aumento: {valor_aumento: .2f}")
print(f"Seu novo salario é: {salario_final: .2f}") 
