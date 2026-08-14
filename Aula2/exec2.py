#Condição lógica usando ternário#

idade = int(input("Informe sua idade: "))
maior_idade = idade >= 18
print("Voce é maior de idade") if maior_idade else print("Voce é menor de idade")

#Usando if e else#

idade = int(input("Informe sua idade: "))
maior_idade = idade >= 18
if maior_idade:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
