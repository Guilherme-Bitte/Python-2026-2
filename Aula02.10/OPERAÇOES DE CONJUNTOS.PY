vazio = set()
data_scientist = set(['Python', 'R', 'SQL', 'Git'])
print(f"A lista A é: {data_scientist}")
data_enginner = {'Python', 'Java', 'Scala', 'Git'}
print(f"A lista B é: {data_enginner}")
#Operaçoes de conjuntos
print(f"A união é: {data_scientist.union(data_enginner)}")
print(f"A interseção é: {data_scientist.intersection(data_enginner)}")
print(f"A diferença é: {data_scientist.difference(data_enginner)}")
print(f"A diferença simetrica é: {data_scientist.symmetric_difference(data_enginner)}")